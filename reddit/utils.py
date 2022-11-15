import praw
import yaml

# from models import Submission, Redditor

from .models import Submission, Redditor

# with open("D:/Dev/Python/django/unilink/static/oauth.yaml", "r") as yamlfile:
#     temp_auth_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
with open("static/oauth.yaml", "r") as yamlfile:
    temp_auth_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

reddit_auth_creds = temp_auth_data["REDDIT"]

reddit = praw.Reddit(
    client_id=reddit_auth_creds["CLIENT_ID"],
    client_secret=reddit_auth_creds["CLIENT_SECRET"],
    password=reddit_auth_creds["PASSWORD"],
    user_agent=reddit_auth_creds["USER_AGENT"],
    username=reddit_auth_creds["USERNAME"],
)


def map_submission(submission):
    mapped_submission = Submission(
        submission.author,
        submission.author_flair_text,
        submission.clicked,
        submission.comments,
        submission.created_utc,
        submission.distinguished,
        submission.edited,
        submission.id,
        submission.is_original_content,
        submission.is_self,
        submission.link_flair_text,
        submission.locked,
        submission.name,
        submission.num_comments,
        submission.over_18,
        submission.saved,
        submission.score,
        submission.selftext,
        submission.spoiler,
        submission.stickied,
        submission.subreddit,
        submission.title,
        submission.upvote_ratio,
        submission.url,
    )
    return mapped_submission


def map_redditor(redditor_object):
    mapped_redditor = Redditor(
        redditor_object.comment_karma,
        redditor_object.comments,
        redditor_object.submissions,
        redditor_object.created_utc,
        redditor_object.has_verified_email,
        redditor_object.icon_img,
        redditor_object.id,
        redditor_object.is_employee,
        redditor_object.is_friend,
        redditor_object.is_mod,
        redditor_object.is_gold,
        redditor_object.link_karma,
        redditor_object.name,
        redditor_object.subreddit,
    )
    return mapped_redditor


def get_new_post(rslash):
    subreddit = reddit.subreddit(rslash)
    for submission in subreddit.new(limit=1):
        mapped_submission = map_submission(submission)
        return mapped_submission


def get_hot_post(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    c = 0
    for submission in subreddit.hot(limit=2):
        if c == 0:
            c += 1
            continue
        mapped_submission = map_submission(submission)
        return mapped_submission


def get_top_post(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    for submission in subreddit.top(limit=1):
        mapped_submission = map_submission(submission)
        return mapped_submission


def get_redditor_by_username(redditor_name):
    redditor_object = reddit.redditor(redditor_name)
    return map_redditor(redditor_object)
