#!/usr/bin/python3
''' returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit '''


import requests


def number_of_subscribers(subreddit):
    reddit_api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "aUserAgent"}
    response = requests.get(reddit_api, headers=headers)
    if response:
        dictio = response.json()
        for i, j in dictio.items():
            if i == "data":
                for k, l in j.items():
                    if k == "subscribers":
                        return l
    return 0
