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
