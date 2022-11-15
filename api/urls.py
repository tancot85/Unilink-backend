from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("twitter/", include("twitter.urls")),
    path("reddit/", include("reddit.urls")),
]
