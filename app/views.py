import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .utils import get_user_data_from_username, get_most_recent_tweets
from .models import TwitterUser, Tweet
import json

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


def get_recent_tweets(request):
    if request.GET:
        name = request.GET.get("name")
        no_of_tweets = request.GET.get("tweets")
        if no_of_tweets == 0:
            no_of_tweets = 5
        final_tweets = []
        tweets = get_most_recent_tweets(name, no_of_tweets)
        for tweet in tweets.data:

            tweet_context_annotations = {}

            tweet_id = tweet.id
            tweet_text = tweet.text
            tweet_edit_history_tweet_ids = (
                True if tweet.edit_history_tweet_ids else None
            )
            tweet_temp_context_annotations = tweet.context_annotations
            tweet_attachments = True if tweet.attachments else False

            for context in tweet_temp_context_annotations:

                domain_name = context["domain"]["name"]
                entity_name = context["entity"]["name"]

                if not domain_name in tweet_context_annotations:
                    tweet_context_annotations[domain_name] = []

                tweet_context_annotations[domain_name].append(entity_name)

            tweet_created_at = tweet.created_at
            tweet_in_reply_to_user_id = True if tweet.in_reply_to_user_id else False
            tweet_possibly_sensitive = tweet.possibly_sensitive
            tweet_retweet_count = tweet.public_metrics["retweet_count"]
            tweet_reply_count = tweet.public_metrics["reply_count"]
            tweet_like_count = tweet.public_metrics["like_count"]
            tweet_quote_count = tweet.public_metrics["quote_count"]

            final_tweet = Tweet(
                tweet_id,
                tweet_text,
                tweet_edit_history_tweet_ids,
                tweet_context_annotations,
                tweet_attachments,
                tweet_created_at,
                tweet_in_reply_to_user_id,
                tweet_possibly_sensitive,
                tweet_retweet_count,
                tweet_reply_count,
                tweet_like_count,
                tweet_quote_count,
            )

            final_tweets.append(final_tweet)
        res = []
        for i in final_tweets:
            converted = i.to_dict()
            res.append(converted)

        return JsonResponse(res, safe=False)
    return HttpResponse("no name specified for retrieving tweets")
