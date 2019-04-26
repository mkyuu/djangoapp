from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True,null=True)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Books(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=800)
    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
