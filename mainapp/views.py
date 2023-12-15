from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.http import Http404

from .models import Article, Comment
from .forms import NewArticle, NewComment

def main_view(request):
    all_articles = Article.objects.all()[::-1]
    top_articles = all_articles[:10]
    return render(request, "mainapp/base.html", {"all_articles":all_articles, "top_articles":top_articles})

# login required do dodawania komentarzy tylko
def read_article_view(request, article_url):
    article = get_object_or_404(Article, url=article_url)
    comments = Comment.objects.filter(article=article)
    if request.method == "POST":
        form = NewComment(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.publication_date = timezone.now()
            new_comment.article = article
            new_comment.owner = request.user
            new_comment = form.save()
            form = NewComment()
    else:
        form = NewComment()
    return render(request, "mainapp/read_article_view.html", {"article":article, "comments":comments, "comment_form":form})

@login_required
def new_article_view(request):
    if request.method == "POST":
        form = NewArticle(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.publication_date = timezone.now()
            new_article.owner = request.user
            new_article = form.save()
            return HttpResponseRedirect(reverse("mainapp:read_article_view", args=(new_article.url,)))
    else:
        form=NewArticle()
        return render(request, "mainapp/new_article_view.html", {"form":form})

@login_required
def edit_article_view(request, article_url):
    article = get_object_or_404(Article, url=article_url)
    if article.owner != request.user:
        raise Http404
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

def user_profile(request, user_username):
    user = get_object_or_404(User, username = user_username)
    activities = []
    articles = Article.objects.filter(owner=user)
    comments = Comment.objects.filter(owner=user)

    # Merge articles and comments into a single list
    for item in articles:
        activities.append(item)

    for item in comments:
        activities.append(item)

    # Sort activities by publication_date from newest to oldest
    activities.sort(key=lambda activity: activity.publication_date, reverse=True)
    return render(request, "mainapp/user_profile.html", {"user":user, "articles":articles, "comments":comments, "activities":activities})
