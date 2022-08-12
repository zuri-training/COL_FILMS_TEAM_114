from django.db import models
from django import forms
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

ACCOUNT_TYPE = (
    ('','select'),
    ('Viewer','Viewer'),
    ('Student', 'Student')
)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_type = models.CharField(max_length=10)

    school = models.CharField(max_length=100,null=True, blank=True, verbose_name="school")

    gender = models.CharField(max_length=10)

    #these are extended models features
    #user_type = models.CharField(max_length=6,null=True)

    avatar = models.FileField(upload_to='avatar/', null=True, blank=True, verbose_name="Avatar")

    def __str__(self):
        return self.user.username


class Movie(models.Model):
    # define a username filed with bound  max length it can have

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True, null=True, verbose_name="Description")

    # This is used to get the video
    video = models.FileField(upload_to='videos/', null=True, verbose_name="") 

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    liked = models.ManyToManyField(User, related_name='liked', default=None, blank=True)

    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    class Meta:
        """Special Class to return plural of Movies"""
        verbose_name_plural = 'movies'    

    
    def __str__(self):
        return f"{self.title} - {self.video} - {self.author} " 

    @property
    def num_likes(self):
        return self.liked.count()

LIKE_CHOICES = (
    ("Like", "Like"),
    ("Unlike", "Unlike"),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=10)

    def __str__(self):
        return self.movie

class MovieComment(models.Model):
    """Comment on a Movie"""

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)  
    comment_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Special Class to return plural of Entry"""
        verbose_name_plural = 'comments'

class School(models.Model):
    school_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.school_name}" 