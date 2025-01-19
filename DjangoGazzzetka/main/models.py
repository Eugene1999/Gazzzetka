import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Using default Django User model
class User(AbstractUser):
    pass


class ThemeColor(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    primary = models.CharField(max_length=7)
    secondary = models.CharField(max_length=7)
    background = models.CharField(max_length=7)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Channel(models.Model):
    theme_color = models.ForeignKey(ThemeColor, on_delete=models.SET_NULL, null=True, related_name='channels')
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='channels')

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='articles')
    source_url = models.URLField()
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    content = models.TextField()
    is_starred = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['author', 'channel']),
        ]

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.article.title}"


class ArticleRelease(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='releases')
    is_active = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)
    release_at = models.DateTimeField(null=True, blank=True)
    released_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['is_active', 'is_released']),
        ]

    def __str__(self):
        return f"Release for {self.article.title}"
