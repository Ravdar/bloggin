from django.contrib import admin
from .models import Article, Comment
from users.models import Profile

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Profile)
# Register your models here.
