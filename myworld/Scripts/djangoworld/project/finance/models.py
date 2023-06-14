from django.db import models

# Create your models here.

class USERS(models.Model) :
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    MailID = models.EmailField(max_length=50)
    Password = models.TextField(max_length=10)