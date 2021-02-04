#!/usr/bin/python3
""" Get Reddit API And display first n titles """
import json
import requests


def top_ten(subreddit):
    """ Func to return n tittles """
    url = "https://www.reddit.com/r/{}/hot.json?count=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS "
               "10_3 like Mac OS X) AppleWebKit/602.1.50"
               " (KHTML, like Gecko) CriOS/56.0.2924.75 "
               "Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0 v8554859393 "
               "t1099441676816697146 ath9b965f92 altpub cvcv=2"}
    response = requests.get(url, headers=headers)
    fullDirection = response.json().get('data').get('children')
    count = 0
    if response.status_code == 200:
        for i in fullDirection:
            if count == 10:
                break
            print(i.get("data").get("title"))
            count += 1
    else:
        print('None')
