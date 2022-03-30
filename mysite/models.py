from django.db import models #Database
from django.utils import timezone #時區
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField #富文本編輯器 CKEditor
from django.conf import settings
from django.db.models.fields.files import ImageFieldFile
import os

# Create your models here.
#設定資料欄位

#class Profile(models.Model):
#    user = models.OneToOneField(User, settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True) #一對一關係擴展
#    def __str__(self):
#        return self.user.username

class User(models.Model):
    username = models.CharField('帳號', max_length=16, unique=True)
    password = models.CharField('密碼', max_length=16)
    email = models.EmailField('電子郵件', unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['c_time']  #降序排列
        verbose_name = '會員'
        verbose_name_plural = '會員'

    def __str__(self):  # 顯示會員名稱用
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Country(models.Model):
    country_id = models.IntegerField()
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class RichPost(models.Model):
    title = models.CharField(max_length=50, default='')
    content = RichTextField(blank=True, max_length=300)
    pub_date = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #classification = models.ManyToManyField(Classification)

class Photo(models.Model):
    pictitle = models.TextField(max_length=50, default="")
    piccontent = models.TextField(default="",blank=True,null=True)
    image = models.ImageField('插入圖片',upload_to='works/', blank=True, null=True)
    upload_date = models.DateField(default=timezone.now,blank=True)

class Expense(models.Model):
    name = models.CharField(max_length=255)  #花費項目
    price = models.IntegerField() #金額