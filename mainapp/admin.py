from django.contrib import admin
from .models import Article, Comment, Subcomment, Topic
from users.models import Profile

admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Topic)

class SubcommentInline(admin.TabularInline):
    model = Subcomment
    extra = 1

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [SubcommentInline]

admin.site.register(Subcomment)
# Register your models here.
