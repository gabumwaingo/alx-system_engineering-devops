#!/usr/bin/python3
"""queries number of subscribers in a subreddit"""

import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    # URL for the subreddit's about page
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0  # Return 0 for invalid subreddits or errors
