#!/usr/bin/python3
""" queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None. """
import json
import requests


def count_words(subreddit, word_list, after=None, answer_dict={}):
        """ Returns list of titles of all hot articles or None """

        url = "https://www.reddit.com/r/{}/hot.json".format(
                subreddit)
        headers = {"User-Agent": "user"}
        parameters = {"show": "all", "next": "next", "after": after}
        response = requests.get(
                url, headers=headers, allow_redirects=False,
                params=parameters).json()

        for item in word_list:
                if item.lower() not in answer_dict:
                        answer_dict[item.lower()] = 0

        if "data" not in response:
                return
        else:
                for i in response.get("data")["children"]:
                        check_list = i["data"]["title"].split()
                        for key, value in answer_dict.items():
                                for item in check_list:
                                        if key == item.lower():
                                                answer_dict[key] += 1
                after = response.get("data").get("after")
                if not after:
                        for key, value in answer_dict.items():
                                print("{}: {}".format(key, value))
                        return
                return count_words(subreddit, word_list, after, answer_dict)
