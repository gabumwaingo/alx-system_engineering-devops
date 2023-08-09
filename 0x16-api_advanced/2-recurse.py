#!/usr/bin/python3
"""A recursive function that queries the reddit api
and returns titles of hot articles"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                hot_list.append(title)
            new_after = data['data']['after']
            if new_after is not None:
                recurse(subreddit, hot_list, new_after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
