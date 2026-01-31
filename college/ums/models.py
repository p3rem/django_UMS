from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    dept = models.CharField(max_length=50)
    phno=models.IntegerField(max_length=15)
    class Meta:
        db_table = "student"

class about(models.Model):
    cname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established_year = models.IntegerField()
    mission=models.TextField()
    vision=models.TextField()
    class Meta:
        db_table = "about"


class contact(models.Model):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message=models.TextField()
    class Meta:
        db_table = "contact"

