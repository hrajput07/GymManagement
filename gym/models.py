from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    emailid = models.CharField(max_length=30)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    emailid = models.EmailField()
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    plan = models.CharField(max_length=50)
    joindate =  models.CharField(max_length=20)
    expiredate =  models.CharField(max_length=20)
    initialamount =  models.CharField(max_length=20)

    def __str__(self):
        return self.name