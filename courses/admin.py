from django.contrib import admin
from .models import (User, Category, Course,
                     Tag, Lesson, Comment,
                     Action, Rating)
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Action)
admin.site.register(Rating)