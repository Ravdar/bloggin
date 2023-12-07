from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    body = models.TextField()
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
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    text = models.TextField()
    publication_date = models.DateField()
    last_edit_date = models.DateField(null=True, blank=True)

    def ___str___(self):
        return self.text