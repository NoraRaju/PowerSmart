from django.db import models
from datetime import date

# Create your models here.

class Login(models.Model) :
    UserName = models.CharField(max_length=30)
    MailID = models.EmailField(max_length=50, default="abc@gmail.com")
    Age = models.IntegerField(null=True)
    DOB = models.DateField(default=date.today, null=True)
    PhnNo = models.BigIntegerField(null=True)
    Password = models.TextField(max_length=10, null=True)
