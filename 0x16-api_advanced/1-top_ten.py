#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit """
import json
import requests


def top_ten(subreddit):
        """ Prints titles of first 10 hot posts for subreddit or None """

        url = "https://www.reddit.com/r/{}/hot.json".format(
                subreddit)
        headers = {"User-Agent": "user"}
        response = requests.get(
                url, headers=headers, allow_redirects=False).json()

        if "data" not in response:
                print(None)
        else:
                items = response.get("data")["children"]
                for i in range(10):
                        print(items[i]["data"]["title"])
