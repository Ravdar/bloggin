from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse

from .models import Article, Comment
from .forms import NewArticle, NewComment

def main_view(request):
    all_articles = Article.objects.all()[::-1]
    return render(request, "mainapp/base.html", {"all_articles":all_articles})

def read_article_view(request, article_url):
    article = get_object_or_404(Article, url=article_url)
    comments = Comment.objects.filter(article=article)
    if request.method == "POST":
        form = NewComment(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.publication_date = timezone.now()
            new_comment.article = article
            new_comment = form.save()
            form = NewComment()
    else:
        form = NewComment()
    return render(request, "mainapp/read_article_view.html", {"article":article, "comments":comments, "comment_form":form})


def new_article_view(request):
    if request.method == "POST":
        form = NewArticle(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.publication_date = timezone.now()
            new_article = form.save()
            return HttpResponseRedirect(reverse("mainapp:read_article_view", args=(new_article.url,)))
    else:
        form=NewArticle()
        return render(request, "mainapp/new_article_view.html", {"form":form})


def edit_article_view(request, article_url):
    article = get_object_or_404(Article, url=article_url)
    if request.method =="POST":
        form = NewArticle(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.last_edit_date = timezone.now()
            article = form.save()
            return HttpResponseRedirect(reverse("mainapp:read_article_view", args=(article.url,)))
    else:
        form = NewArticle(instance=article)
    return render(request, "mainapp/edit_article_view.html", {"form": form})

# def user_profile_view(request, user_id):

# def sign_up_view(request):

# def login_view(request):
