from django.contrib import admin

# Register your models here.
from .models import User, ThemeColor, Channel, Article, ArticleImage, ArticleRelease

admin.site.register(User)
admin.site.register(ThemeColor)
admin.site.register(Channel)
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(ArticleRelease)
