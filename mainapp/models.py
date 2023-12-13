from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    publication_date = models.DateField()
    last_edit_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    url = models.CharField(max_length=200, default='doesnotwork')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        words = self.title.split()[:5]
        self.url = slugify('-'.join(words).lower())
        super().save(*args, **kwargs)

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateField()
    last_edit_date = models.DateField(null=True, blank=True)

class Subcomments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateField()
    last_edit_date = models.DateField(null=True, blank=True)
    
    

    def ___str___(self):
        return self.text