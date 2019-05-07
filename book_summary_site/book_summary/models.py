from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


class BigCategory(models.Model):
    name = models.CharField('カテゴリ名',max_length=100)

class Category(models.Model):
    name = models.CharField('ジャンル名',max_length=100)
    bigcategory = models.ForeignKey(BigCategory,on_delete=models.SET_NULL,null=True,verbose_name='カテゴリ名')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('著者名',max_length=50)

class Publisher(models.Model):
    name = models.CharField('出版社名',max_length=50)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.name

class Book(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField('タイトル',max_length=100)
    summary = models.TextField('要約')
    img = models.URLField('画像url',blank=True)
    link = models.URLField('Amazonリンク',blank=True)
    published_date = models.DateTimeField('公開日',blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='ジャンル')
    publisher = models.ForeignKey(Publisher,on_delete=models.PROTECT,blank=True,verbose_name='出版社')
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,blank=True)
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(verbose_name='タイトル',max_length=200)
    comment = models.TextField(verbose_name='コメント')
    published_date = models.DateTimeField(verbose_name='公開日',auto_now_add=timezone.now())
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title

class Good(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
