import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .utils import get_user_data_from_username
from .models import TwitterUser

# Create your views here.


def hello(requeset):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    ans = {"name": "some"}
    return JsonResponse(ans)


def get_user_details(request):
    if request.GET:
        name = request.GET.get("name")
        user_data = get_user_data_from_username(name)
        user = TwitterUser(
            user_data.data.id,
            user_data.data.username,
            user_data.data.name,
            user_data.data.created_at,
            user_data.data.description,
            user_data.data.pinned_tweet_id,
            user_data.data.profile_image_url,
            user_data.data.protected,
            user_data.data.public_metrics["followers_count"],
            user_data.data.public_metrics["following_count"],
            user_data.data.public_metrics["tweet_count"],
            user_data.data.verified,
            user_data.data.location,
        )
        return JsonResponse(user.to_dict())
    return HttpResponse("no value entered")
