from django.urls import path
from . import views


app_name = "mainapp"
urlpatterns = [path("", views.main_view, name="main_view"),
               path("hello/", views.hello_visitor, name="hello_visitor"),
               path("new_article/", views.new_article_view, name="new_article_view"),
               path("<str:article_url>/", views.read_article_view, name="read_article_view"), 
               path("edit/<str:article_url>/", views.edit_article_view, name="edit_article_view"),
               path("users/<str:user_username>/", views.user_profile, name="user_profile"),] 