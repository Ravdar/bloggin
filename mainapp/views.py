from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.http import Http404, JsonResponse

from .models import Article, Comment, ArticleVote, Topic, Subcomment
from .forms import NewArticle, NewComment, NewSubcomment

def main_view(request):
    """Home page view, returns all articles ordered from the newest, list of top articles and available topics.
    """
    all_articles = Article.objects.all()[::-1]
    top_articles = Article.objects.all()[:10]
    topics = Topic.objects.all()
    return render(request, "mainapp/main.html", {"all_articles":all_articles, "top_articles":top_articles, "topics":topics})


def read_article_view(request, article_url):
    """View for displaying article content and comment/subcomment forms."""

    # Acces specific article and it's comments
    article = get_object_or_404(Article, url=article_url)
    comments = Comment.objects.filter(article=article)

    # Handling submitting a comment
    if request.method == "POST":
        comment_form = NewComment(request.POST)
        subcomment_form = NewSubcomment(request.POST)
        form_type = request.POST.get('form_type')
        if form_type == 'comment_form':
            # If submit is a comment
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.publication_date = timezone.now()
                new_comment.article = article
                new_comment.owner = request.user
                new_comment.save()            
        elif form_type == 'subcomment_form':
            # If submit is subcomment
            if subcomment_form.is_valid():
                parent_comment_id = request.POST.get('parent_comment_id')
                parent_comment = get_object_or_404(Comment, pk=parent_comment_id)
                new_subcomment = subcomment_form.save(commit=False)
                new_subcomment.publication_date = timezone.now()
                new_subcomment.article = article
                new_subcomment.owner = request.user
                new_subcomment.parent_comment = parent_comment
                new_subcomment.save()
        comment_form = NewComment()
        subcomment_form = NewSubcomment()
        return render(request, "mainapp/read_article.html", {
            "article": article,
            "comments": comments,
            "comment_form": comment_form,
            "subcomment_form": subcomment_form
        })
    else:
        # Display article and comments forms (GET request)
        comment_form = NewComment()
        subcomment_form = NewSubcomment()

    return render(request, "mainapp/read_article.html", {
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
        "subcomment_form": subcomment_form
    })


@login_required
def new_article_view(request):
    """View for adding new article."""

    # Submitting article (POST request)
    if request.method == "POST":
        form = NewArticle(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.publication_date = timezone.now()
            new_article.owner = request.user
            new_article = form.save()
            return HttpResponseRedirect(reverse("mainapp:read_article_view", args=(new_article.url,)))
    #GET request
    else:
        form=NewArticle()
        return render(request, "mainapp/new_article.html", {"form":form})


@login_required
def edit_article_view(request, article_url):
    """View for editing already existing article."""

    # Acces specific article
    article = get_object_or_404(Article, url=article_url)
    # Check if user is the owner of the article, so he can edit it
    if article.owner != request.user:
        raise Http404
    # POST request
    if request.method =="POST":
        form = NewArticle(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.last_edit_date = timezone.now()
            article = form.save()
            return HttpResponseRedirect(reverse("mainapp:read_article_view", args=(article.url,)))
    # Displaying article content in form (GET request)
    else:
        form = NewArticle(instance=article)
    return render(request, "mainapp/edit_article_view.html", {"form": form})


def user_profile(request, user_username):
    """Displaying profile of specific user, his info such as nickname, profile picture, added articles and comments."""

    # Acces user and his activities
    user = get_object_or_404(User, username = user_username)
    activities = []
    articles = Article.objects.filter(owner=user)
    comments = Comment.objects.filter(owner=user)
    subcomments = Subcomment.objects.filter(owner=user)

    # Merge articles and comments into a single list
    for item in articles:
        activities.append(item)

    for item in comments:
        activities.append(item)

    for item in subcomments:
        activities.append(item)

    # Sort activities by publication_date from newest to oldest
    if activities != []:
        activities.sort(key=lambda activity: activity.publication_date, reverse=True)
    return render(request, "mainapp/user_profile.html", {"user":user, "articles":articles, "comments":comments, "activities":activities})
