import datetime

from django.db import models


class User(models.Model):
    id = models.AutoField
    email = models.EmailField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    full_name = models.CharField(max_length=150)
    signup = models.DateTimeField(default=datetime.date.today())
    logins = models.IntegerField(default=0)
    last_login = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.email

