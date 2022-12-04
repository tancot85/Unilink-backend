from . import views
from django.urls import include, path

urlpatterns = [
    path("home/", views.hello, name="hello"),
    path("user/", views.get_user_details, name="get_user_details"),
    path("tweets/", views.get_recent_tweets, name="get_recent_tweets"),
    path("login_receive/",views.login_receive,name="login_receive")
]
