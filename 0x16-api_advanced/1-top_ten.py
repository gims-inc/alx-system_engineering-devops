#!/usr/bin/python3
""" Number of subreddits """

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"user-agent": "my-app/0.0.1"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None
    try:
        data = response.json()
    except ValueError:
        return None
    try:
        children = data["data"]["children"]
        for child in children[:10]:
            post = child["data"]["title"]
            print(post)
    except Exception:
        return None
