#!/usr/bin/python3
""" Number of subreddits """

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "my-app/0.0.1"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    try:
        data = response.json()
    except ValueError:
        return 0

    subscribers = data["data"]["subscribers"]

    if subscribers:
        return subscribers
