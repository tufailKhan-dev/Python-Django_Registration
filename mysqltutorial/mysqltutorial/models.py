from django.db import models

class mysqldata(models.Model):

    employeeNumber = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    jobTitle = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    extension = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    officeCode = models.CharField(max_length=100)
    reportsTo = models.CharField(max_length=100)
    
    class Meta:
        db_table="employees"
