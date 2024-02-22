from django import forms
from .models import Article, Comment, Subcomment, Topic

class NewArticle(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(queryset=Topic.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Article
        fields = ["title", "body","image", "topics"]

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

class NewSubcomment(forms.ModelForm):
    class Meta:
        model = Subcomment
        fields=["text"]
        