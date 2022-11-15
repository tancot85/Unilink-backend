from . import views
from django.urls import include, path

urlpatterns = [
    path("hello/", views.hello_reddit, name="hello"),
    path("get_post/", views.get_post, name="get_post"),
    path("get_redditor/", views.get_redditor, name="get_redditor"),
]
