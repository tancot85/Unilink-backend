from . import views
from django.urls import include, path

urlpatterns = [
    path("home/", views.hello, name="hello"),
    path("twitter/", views.get_user_details, name="get_user_details"),
]
