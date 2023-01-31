#!/usr/bin/python3
""" Top ten subreddits """

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"user-agent": "my-app/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    children = data["data"]["children"]
    for child in children[:10]:
        post = child["data"]["title"]
        print(post)
