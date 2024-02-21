from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Topic(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    publication_date = models.DateField()
    last_edit_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    url = models.CharField(max_length=200, default='doesnotwork')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        words = self.title.split()[:5]
        self.url = slugify('-'.join(words).lower())
        self.total_votes = self.upvotes - self.downvotes
        super().save(*args, **kwargs)
    
    def update_total_votes(self):
        self.upvotes = ArticleVote.objects.filter(article=self, is_upvote=True).count()
        self.downvotes = ArticleVote.objects.filter(article=self, is_upvote=False).count()
        self.save()

class ArticleVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()
    
    class Meta:
        unique_together = ('user', 'article')

    def save(self, *args, **kwargs):
        existing_vote = ArticleVote.objects.filter(user=self.user, article=self.article)
        if existing_vote:
            existing_vote.is_upvote = self.is_upvote
            existing_vote.save()
        else:
            super().save(*args, **kwargs)

            if self.is_upvote:
                self.article.upvotes +=1
            else:
                self.article.downvotes +=1
            self.article.save()


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateField()
    last_edit_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.text
    

class Subcomment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(Comment, related_name="subcomments", on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateField()
    last_edit_date = models.DateField(null=True, blank=True)

    def ___str___(self):
        return self.text
    

