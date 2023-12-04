from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Article
from .forms import NewArticle

def main_view(request):
    all_articles = Article.objects.all()[::-1]
    return render(request, "mainapp/main_view.html", {"all_articles":all_articles})

# def read_article_view(request, article_id):

def new_article_view(request):
    if request.method == "POST":
        form = NewArticle(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.publication_date = timezone.now()
            new_article = form.save()
            return HttpResponseRedirect(reverse("mainapp:read_article_view", args=(new_article.url)))
    else:
        form=NewArticle()
        return render(request, "mainapp/new_article_view.html", {"form":form})



# def edit_article_view(request):

# def user_profile_view(request, user_id):

# def sign_up_view(request):

# def login_view(request):
