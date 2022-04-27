from django.db import models

# Create your models here.
class Types(models.Model):
    title = models.CharField('name', max_length=255),
    content = models.TextField('text'),

    def __str__(self):
        return self.title
