from django.conf import settings
from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField('name', max_length=250)
    info = models.TextField('text')
    link = models.URLField(max_length=200)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курстар'
        ordering = ['name']

class Comment(models.Model):
    username = models.CharField('user', max_length=200)
    text = models.TextField('comment')
    date_at = models.DateTimeField('publication date')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return '/news/comments'
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарийлер'
        ordering = ['date_at', 'username']

class News(models.Model):
    name = models.CharField('name', max_length=200)
    text = models.TextField('text')
    date_at = models.DateTimeField('publication date')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жаңалық'
        verbose_name_plural = 'Жаңалықтар'
        ordering = ['date_at', 'name']

class Authorizing(models.Model):
    username = models.CharField('user', max_length=200)
    surname = models.CharField('surname', max_length=200)
    education = models.CharField('education', max_length=300)
    birth_date = models.DateField('birthday date')
    password = models.CharField('password', max_length=200)
    city = models.CharField('city', max_length=200)
    email = models.EmailField('email', max_length=300)
    phone = models.CharField('phone number', max_length=400)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return '/news/authorize'
    class Meta:
        verbose_name = 'Қолданушы'
        verbose_name_plural = 'Қолданушылыр'

