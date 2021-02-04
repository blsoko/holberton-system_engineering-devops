#!/usr/bin/python3
""" Get Reddit API And display n subs """
import json
import requests


def number_of_subscribers(subreddit):
    """ Func to return n subs """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS "
               "10_3 like Mac OS X) AppleWebKit/602.1.50"
               " (KHTML, like Gecko) CriOS/56.0.2924.75 "
               "Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0 v8554859393 "
               "t1099441676816697146 ath9b965f92 altpub cvcv=2"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
