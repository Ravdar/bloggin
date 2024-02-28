from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.http import Http404, JsonResponse

from .models import Article, Comment, ArticleVote, Topic, Subcomment
from .forms import NewArticle, NewComment, NewSubcomment

def main_view(request):
    all_articles = Article.objects.all()[::-1]
    top_articles = all_articles[:10]
    topics = Topic.objects.all()
    return render(request, "mainapp/main_refactor.html", {"all_articles":all_articles, "top_articles":top_articles, "topics":topics})

# Handling AJAX requests on articles votes
def vote_article(request):
    if request.method == 'POST' and request.is_ajax():
        article_id = request.POST.get('article_id')
        is_upvote = request.POST.get('is_upvote')
        article = Article.objects.get(pk=article_id)
        user = request.user

        # Check if the user has already voted on this article
        existing_vote = ArticleVote.objects.filter(user=user, article=article).first()
        if existing_vote:
            existing_vote.is_upvote = is_upvote
            existing_vote.save()
        else:
            # Create a new vote
            ArticleVote.objects.create(user=user, article=article, is_upvote=is_upvote)

        # Update the article's vote count
        article.update_total_votes()

        # Return JSON response with updated vote counts
        return JsonResponse({'success': True, 'upvotes': article.upvotes, 'downvotes': article.downvotes})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


# login required only for adding comments
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
            comment_form = NewComment()
            subcomment_form = NewSubcomment()
    else:
        comment_form = NewComment()
        subcomment_form = NewSubcomment()
    return render(request, "mainapp/read_article_view.html", {"article":article, "comments":comments, "comment_form":comment_form, "subcomment_form":subcomment_form})

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
        return render(request, "mainapp/new_article_refactor.html", {"form":form})

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
    return render(request, "mainapp/user_profile_refactored.html", {"user":user, "articles":articles, "comments":comments, "activities":activities})
