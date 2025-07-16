import itertools
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Blog(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')

    # Blog content
    blog_title = models.CharField(max_length=264, verbose_name='blog_title')
    slug = models.SlugField(max_length=264, unique=False, blank=True)
    content = models.TextField(verbose_name='blog_content')
    blog_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.blog_title} by {self.author.username}"

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            base_slug = slugify(self.blog_title)
            
        super().save(*args, **kwargs)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField(verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.blog_title}"


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blog', 'user')  # prevent double-likes

    def __str__(self):
        return f"{self.user.username} liked {self.blog.blog_title}"
