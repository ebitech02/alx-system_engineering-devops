#!/usr/bin/python3

"""
This script fetches the total number of subscribers for
given subreddit. If invalid subreddit is given, the function should
return 0.


Modules used:
    - json: For parsing JSON data.
    - urllib.error: For catching errors when code fails.
    - urllib.request: For making HTTP requests.

"""

import json
import urllib.error
import urllib.request


def number_of_subscribers(subreddit):
    """
    Description: Get the total subscribers for a subreddit.


    Args:
       subreddit (str): Subreddit to check

    Returns:
       int: total subscribers or 0 if invalid.
       """

   # URL to fetch
   url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

   # to avoid too many requests
   headers = {'User-Agent': 'Mozilla/5.0'}
    # A request object with custom headers
    request = 
        urllib.request.\
        Request(url, headers=headers, allow_redirects=False)
    try:
        with urllib.request.urlopen(request) as response:
            if response.status_code == 200:
                data = json.loads(response.read().decode())
                return data['data']['subscribers']
            else:
                return 0
    except (urllib.error.HTTPError, urllib.error.URLError):
        return 0
