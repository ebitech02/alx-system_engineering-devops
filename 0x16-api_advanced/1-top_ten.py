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
        if response.status_code != 200 or 'application/json' \
                not in response.headers.get('Content-Type', ''):
            print(None)
            return
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Print the titles of the top 10 posts
        for i in range(min(10, len(posts))):
            print(posts[i]['data']['title'])

    except requests.RequestException:
        print(None)
