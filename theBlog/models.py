from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank = True, upload_to="images/")
    post_date = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length=50, default='random')
    snippet = models.CharField(max_length=15, default='Click to read more')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank = True, upload_to="images/upload")
    website_url = models.CharField(max_length=80, null=True, blank=True)
    email_url = models.CharField(max_length=80, null=True, blank=True)
    facebook_url = models.CharField(max_length=80, null=True, blank=True)
    twitter_url = models.CharField(max_length=80, null=True, blank=True)
    reddit_url = models.CharField(max_length=80, null=True, blank=True)

    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank = True, upload_to="images/")

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)