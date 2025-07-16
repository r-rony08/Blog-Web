from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    # Personal Information
    full_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.CharField(verbose_name='Short Bio',max_length=200,blank=True,help_text='A brief personal summary  (max 255 characters).')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Social Media Links (optional)
    website = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

     # Blog Activity / Stats
    total_posts = models.PositiveIntegerField(default=0)
    total_likes = models.PositiveIntegerField(default=0)
    total_followers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.full_name or self.user.username