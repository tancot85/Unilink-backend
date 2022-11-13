import tweepy
import yaml
import json

with open("app/twitter-oauth.yaml", "r") as yamlfile:
    temp_twitter_auth_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

twitter_auth_creds = temp_twitter_auth_data["TWITTER"]

client = tweepy.Client(
    access_token=twitter_auth_creds["ACCESS_TOKEN"],
    access_token_secret=twitter_auth_creds["ACCESS_TOKEN_SECRET"],
    consumer_key=twitter_auth_creds["COSUMER_KEY"],
    consumer_secret=twitter_auth_creds["CONSUMER_SECRET"],
    bearer_token=twitter_auth_creds["BEARER_TOKEN"],
    wait_on_rate_limit=True,
)


def get_user_data_from_username(screen_name: str):
    user_data = client.get_user(
        username=screen_name,
        user_fields=[
            "created_at",
            "location",
            "description",
            "pinned_tweet_id",
            "profile_image_url",
            "protected",
            "public_metrics",
            "verified",
        ],
    )
    return user_data
