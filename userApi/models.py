from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50 )
    emailid = models.CharField(max_length=50)
    mobileNo = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    