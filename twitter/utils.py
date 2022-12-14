import tweepy
import yaml
import json

with open("static/oauth.yaml", "r") as yamlfile:
    temp_auth_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

twitter_auth_creds = temp_auth_data["TWITTER"]

twitter_client = tweepy.Client(
    access_token=twitter_auth_creds["ACCESS_TOKEN"],
    access_token_secret=twitter_auth_creds["ACCESS_TOKEN_SECRET"],
    consumer_key=twitter_auth_creds["COSUMER_KEY"],
    consumer_secret=twitter_auth_creds["CONSUMER_SECRET"],
    bearer_token=twitter_auth_creds["BEARER_TOKEN"],
    wait_on_rate_limit=True,
)


def get_user_data_from_username(screen_name: str):
    user_data = twitter_client.get_user(
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


def get_most_recent_tweets(name, max_tweets=5):
    print(f"name: {name}")
    user_data = get_user_data_from_username(name)
    print("found user")
    user_id = user_data.data.id
    tweets = twitter_client.get_users_tweets(
        user_id,
        tweet_fields=[
            "attachments",
            "created_at",
            "context_annotations",
            "in_reply_to_user_id",
            "possibly_sensitive",
            "public_metrics",
        ],
        max_results=max_tweets,
    )
    return tweets
