from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


def set_default_bigcategory():
    bigcategory, _ = BigCategory.objects.get_or_create(name='None')
    return bigcategory.pk

def set_default_category():
    category, _ = Category.objects.get_or_create(name='None')
    return category.pk

def set_default_author():
    author, _ = Author.objects.get_or_create(name='unknown')
    return author.pk

def set_default_publisher():
    publisher, _ = Publisher.objects.get_or_create(name='None')
    return publisher.pk


class BigCategory(models.Model):
    name = models.CharField('カテゴリ名',max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('ジャンル名',max_length=100)
    bigcategory = models.ForeignKey(BigCategory,on_delete=models.SET_DEFAULT,default=set_default_bigcategory,verbose_name='カテゴリ名')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('著者名',max_length=50)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField('出版社名',max_length=50)
    author = models.ForeignKey(Author,on_delete=models.SET_DEFAULT,default=set_default_author)


    def __str__(self):
        return self.name

class Book(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    title = models.CharField('タイトル',max_length=100)
    summary = models.TextField('要約')
    img = models.URLField('画像url',blank=True)
    link = models.URLField('Amazonリンク',blank=True)
    published_date = models.DateTimeField('公開日',blank=True,auto_now_add=timezone.now())
    bigcategory = models.ForeignKey(BigCategory,on_delete=models.SET_DEFAULT,default=set_default_bigcategory,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default=set_default_category,blank=True,verbose_name='ジャンル')
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_DEFAULT,default=set_default_publisher,blank=True,verbose_name='出版社')
    author = models.ForeignKey(Author,on_delete=models.SET_DEFAULT,default=set_default_author,blank=True)
        
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    title = models.CharField(verbose_name='投稿者',max_length=200,blank=True,default='名無しさん')
    comment = models.TextField(verbose_name='コメント')
    published_date = models.DateTimeField(verbose_name='公開日',auto_now_add=timezone.now())
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title

class Good(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
