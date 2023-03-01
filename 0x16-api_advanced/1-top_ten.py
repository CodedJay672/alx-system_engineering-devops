#!/usr/bin/python3
"""
function that queries a reddit API and returns number of
subscribers for a given subreddit

"""
import requests


def top_ten(subreddit):
    """function for getting subreddit users"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": 'alx-api_advanced'
    }
    params = {
            "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    results = response.json().get('data')
    [print(c.get('data').get('title')) for c in results.get('children')]
