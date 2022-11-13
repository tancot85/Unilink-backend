from . import views
from django.urls import include, path

urlpatterns = [
    path("home/", views.hello, name="hello"),
    path("twitter_user/", views.get_user_details, name="get_user_details"),
    path("recent_tweets/", views.get_recent_tweets, name="get_recent_tweets"),
]
