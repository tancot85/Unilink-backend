from django.db import models
from dataclasses import dataclass
from datetime import datetime

# Create your models here.
@dataclass(init=True, repr=True, frozen=True)
class Tweet:
    id_: str
    text: str
    edit_history_tweet_ids: bool
    context_annotations: dict
    attachments: bool
    created_at: datetime
    in_reply_to_user_id: bool
    possibly_sensitive: bool
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int

    def to_dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}


class TwitterUser:
    def __init__(
        self,
        id_,
        username,
        name,
        account_creation_date,
        description,
        pinned_tweet,
        profile_image_url,
        is_protected,
        followers_count,
        following_count,
        tweet_count,
        is_verified,
        location,
    ) -> None:

        self.id_ = id_
        self.username = username
        self.name = name
        self.account_creation_date = account_creation_date
        self.location = location
        self.description = description
        self.description_length = len(description)
        self.has_pinned_tweet = True if pinned_tweet else False
        self.profile_image_url = profile_image_url
        self.is_protected = is_protected
        self.followers_count = followers_count
        self.following_count = following_count
        self.tweet_count = tweet_count
        self.is_verified = is_verified

    def __str__(self) -> str:
        return f"""
        id: {self.id_},
        username: {self.username},
        name: {self.name},
        account_creation_date: {self.account_creation_date},
        location: {self.location},
        description: {self.description},
        description_length: {self.description_length},
        has_pinned_tweet: {self.has_pinned_tweet},
        profile_image_url: {self.profile_image_url},
        is_protected: {self.is_protected},
        followers_count: {self.followers_count},
        following_count: {self.following_count},
        tweet_count: {self.tweet_count},
        is_verified: {self.is_verified},
    """

    def to_dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}
