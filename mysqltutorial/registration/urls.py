from django.urls import path
from . import views
urlpatterns = [
    path('',views.Loging,name="login"),
    path('signup/',views.Signing,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
]
