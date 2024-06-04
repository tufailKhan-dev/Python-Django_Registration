from django.core.mail import EmailMessage,send_mail
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from mysqltutorial import settings
from django.core import mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from mysqltutorial.tokens import generate_token
from mysqltutorial.views import index
# Create your views here.

def Loging(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        # condition 
        if len(username) > 10 or len(username) < 3:
            messages.error(request,"username should be proper and complete")
            return redirect("login")
        
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"hello how r u!")
            return redirect('home/')
        else:
            messages.error(request,"something went wrong")
            return redirect("login")

    return render(request,"login.html")

def Signing(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        # condition to create users
        
        if User.objects.filter(username=username):
            messages.error(request,"user already exist! Please try another user name")
            return redirect("signup")
        
        if User.objects.filter(email=email):
            messages.error(request,"email already register plss try another email")
            return redirect("signup")
        
        if len(username) > 10 or len(username) < 3:
            messages.error(request,"username must be less then 10 alphanumeric ")
            return redirect("signup")
           
        if not username.isalnum():
            messages.error(request,"Username must be Alphanumeric!")
            return redirect("signup")
        



        #user created
        user = User.objects.create_user(username,email,password)


        #first user verify himself
        user.is_active = False


        #saving user after email verification
        user.save()

        
        messages.success(request,'confirm ur email , we send u email')

        # welcome messages in gmail
        subject = "welcome to our website thanku for login"
        message = "Hello " + user.username + "!! \n " + "welcome to our website "
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        mail.send_mail(subject, message, from_email, to_list, fail_silently = True)


        #Email confirmation goest here
        current_site = get_current_site(request)
        email_subject = "Confirm your email "
        message2 = render_to_string('email_confirmation.html',{
            'name' : user.username,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : generate_token.make_token(user),
        }) 

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
        )

        email.fail_silently = True
        email.send()
        return redirect('signup')
    return render(request,"signup.html")

def signout(request):
    logout(request)
    messages.success(request,'u successfully logout!!')
    return redirect('login')


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError , OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(request,user)
        messages.success(request,"your account has been created successfully " + "\n  now u can login ")
        return redirect('login')
    else:
        return render(request,'activation_failed.html')


