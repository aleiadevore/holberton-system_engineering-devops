#!/usr/bin/python3
""" queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None. """
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
        """ Returns list of titles of all hot articles or None """

        url = "https://www.reddit.com/r/{}/hot.json".format(
                subreddit)
        headers = {"User-Agent": "user"}
        parameters = {"show": "all", "next": "next", "after": after}
        response = requests.get(
                url, headers=headers, allow_redirects=False,
                params=parameters).json()

        if "data" not in response:
                return None
        else:
                for i in response.get("data")["children"]:
                        hot_list.append(i["data"]["title"])
                after = response.get("data").get("after")
                if not after:
                        return hot_list
                return recurse(subreddit, hot_list, after)
