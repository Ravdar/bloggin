from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    body = models.TextField()
    publication_date = models.DateField()
    last_edit_date = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    url = models.URLField(default='doesnotwork')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        words = self.title.split()[:5]
        self.url = '-'.join(words).lower()
        super().save(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    text = models.TextField()
    publication_date = models.DateField()
    last_edit_date = models.DateField()

    def ___str___(self):
        return self.text