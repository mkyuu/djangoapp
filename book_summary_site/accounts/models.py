from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    gender_choice = (
        ( 1,'男'),
        (2,'女')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField('ユーザーネーム', max_length=20)
    gender = models.CharField(choices=gender_choice,max_length=2)
    birthday = models.DateField(blank=True)
    email = models.EmailField('Email')

    def __str__(self):
        return self.name


class Follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow_user')

    def __str__(self):
        return str(self.user)
