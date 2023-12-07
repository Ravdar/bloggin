from django import forms
from .models import Article, Comment

class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body","image"]

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]
        