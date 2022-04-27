from django.contrib import admin

# Register your models here.
from .models import News
from .models import Comment
from .models import Course
from .models import Authorizing

admin.site.register(News)

admin.site.register(Comment)

admin.site.register(Course)

admin.site.register(Authorizing)