#!/usr/bin/python3
''' prints the titles of the first
    10 hot posts listed
    for a given subreddit '''


import requests


def top_ten(subreddit):
    reddit_api = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit)
    headers = {"User-Agent": "aUserAgent"}
    response = requests.get(reddit_api, headers=headers)
    if response:
        for post in response.json()['data']['children']:
            print(post["data"]["title"])
    else:
        print(None)
