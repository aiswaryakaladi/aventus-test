from django.db import models

# Create your models here.

class employeemodel(models.Model):
    fname=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    photo=models.FileField(upload_to='aveapp/static')
    designation=models.CharField(max_length=30)

