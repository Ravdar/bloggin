from django import forms
from .models import Article, Comment, Subcomment

class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body","image"]

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

class NewSubcomment(forms.ModelForm):
    class Meta:
        model = Subcomment
        fields=["text"]
        