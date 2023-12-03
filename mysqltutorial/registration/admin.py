from django.contrib import admin
from mysqltutorial.models import mysqldata
# Register your models here.
class Register(admin.ModelAdmin):
    list_display = ('employeeNumber','firstName','jobTitle','lastName','extension','email','officeCode','reportsTo')

admin.site.register(mysqldata,Register)
