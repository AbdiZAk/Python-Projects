import requests
import json
from ipywidgets import interact
from dotenv import load_dotenv
import os


def config():
    load_dotenv()


def get_sentiment(text):
    url = 'http://text-processing.com/api/sentiment/'
    payload = {'text': text}
    response = requests.post(url, data=payload)
    sentiment = response.json()
    return sentiment['label']


def get_redit_story(sub):
    url = f"https://www.reddit.com/r/{sub}/top.json?limit=25"
    user = {
        'User-Agent': f'ist256.lesson10.homework:v1.0 (by {os.getenv("reddit_user")})'
    }
    titles = ''
    response = requests.get(url, headers=user)
    response.raise_for_status()
    redit_stories = response.json()
    stories = redit_stories['data']['children']
    for story in stories:
        titles += story['data']['title']

    return titles


subreddits = ['ama', 'aww', 'news', 'worldnews', 'politics', 'todayilearned', 'explainlikeimfive', 'writingprompts',
              'upliftingnews', 'wholesomememes', 'freecompliments', 'happy', 'financialadvice', 'breadit']
subreddits.sort()


# @interact(Subreddit=subreddits)
def main(subreddit):
    load_dotenv()
    title = get_redit_story(subreddit)
    sentiment = get_sentiment(title)
    print(f"The overall sentiemnt of {subreddit} is {sentiment}.")


subreddit = input('Enter a Subreddit: ')
main(subreddit)
