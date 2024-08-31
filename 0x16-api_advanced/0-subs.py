#!/usr/bin/python3

"""
This script fetches the total number of subscribers for a given
subreddit. If an invalid subreddit is given, the function
should return 0.


Modules used:
    - json: For parsing JSON data.
    - urllib.request: For making HTTP requests..

"""

import json
import urllib.request


def number_of_subscribers(subreddit):
    """
    Description: Get the total subscribers for a subreddit


    Args:
        subreddit (str): Subreddit to check

    Returns:
        Int: Total subscribers or 0 if invalid.

    """
    # URL to fetch the data from
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # A custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    # A request object with custom headers
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            return data['data']['subscribers']
        else:
            return 0
