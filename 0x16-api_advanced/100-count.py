#!/usr/bin/python3
""" queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None. """
import json
import requests


def count_words(subreddit, word_list, spot=0):
        """ Returns list of titles of all hot articles or None """

        url = "https://www.reddit.com/r/{}/hot.json".format(
                subreddit)
        headers = {"User-Agent": "user"}
        parameters = {"show": "all", "next": "next"}
        response = requests.get(
                url, headers=headers, allow_redirects=False,
                params=parameters).json()

        if "data" not in response:
                return
        else:
                count = 0
                for i in response.get("data")["children"]:
                        if word_list[spot].lower() in i["data"]["title"].lower():
                                count += 1
                if count > 0:
                        print("{}: {}".format(word_list[spot], count))
                if spot == (len(word_list) - 1):
                        return
                return count_words(subreddit, word_list, spot + 1)
