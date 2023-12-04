from django import forms
from .models import Article

class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body","image"]
        