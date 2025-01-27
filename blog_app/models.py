from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog_app', null=True, blank=True)
    #If author leaves the website, their posts will dissapear
    #Relation one to many
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #Post can have more than one category and viceversa
    #Relation many to many
    categories = models.ManyToManyField(Category)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return str(self.title)
