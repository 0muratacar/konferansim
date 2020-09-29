from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):

    last_login = models.DateTimeField(auto_now=True)
    is_deleted = models.DateTimeField(blank=True, null=True)
    is_active = True
    status = (('author', 'author'), ('editor', 'editor'), ('reader', 'reader'),)
    statu = models.CharField(choices=status, blank=True,
                             null=True, db_index=True, max_length=32)


class Bildiri(models.Model):

    author = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    abstract = models.CharField(max_length=2000)
    full_text = models.TextField()
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)


class Konferans(models.Model):
    participant = models.IntegerField()
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    when = models.DateTimeField()


class Poster(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    desc = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(blank=True, null=True)


class Haberler(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
