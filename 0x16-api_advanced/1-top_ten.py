#!/usr/bin/python3
"""
This scripts queries the API and prints the titles
of the first 10 hot posts
"""


import requests


def top_ten(subreddit):
    """Prints the title of the first 10"""
    url = "https://www.reddit.com/r/{}/hot.json.format(subreddit)"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)
