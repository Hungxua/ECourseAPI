from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')



class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class ItemBase(models.Model):
    class Meta:
        abstract = True

    subject = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.content


class ActionBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Action(ActionBase):
    LIKE, HAHA, HEART = range(3)
    ACTIONS=[
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS,default= LIKE)


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)


class LessonView(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)


