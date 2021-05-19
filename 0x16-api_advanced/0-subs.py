#!/usr/bin/python3
""" queries the Reddit API and returns the number of
subscribers for a given subreddit """
import json
import requests


def number_of_subscribers(subreddit):
        """ Returns number of subscribers or 0 if subreddit doesn't exist """

        """ GET /r/subreddit/aboutread
        Data includes the subscriber count, description, and header image."""

        url = "https://www.reddit.com/r/{}/about.json".format(
                subreddit)
        headers = {"User-Agent": "user"}
        response = requests.get(
                url, headers=headers, allow_redirects=False).json()

        if "data" not in response:
                return 0
        return response.get("data")["subscribers"]
