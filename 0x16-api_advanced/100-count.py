#!/usr/bin/python3
""" Prints number of keywords given for a subreddits hot list """
import json
import requests


def count_words(subreddit, word_list, after=None, answer_dict={}):
        """ Prints number of keywords given for a subreddits hot list """

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
                        for key, value in sorted(
                                answer_dict.items(),
                                key=lambda item: item[1], reverse=True):
                                if value != 0:
                                        print("{}: {}".format(key, value))
                        return
                return count_words(subreddit, word_list, after, answer_dict)
