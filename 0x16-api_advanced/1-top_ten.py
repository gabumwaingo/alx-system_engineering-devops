#!/usr/bin/python3
"""
queries the reddit api and returns a list of tue first 10 hotspots for a subreddit
"""
import requests
import sys

def top_ten(subreddit):
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    
    response = requests.get(url, headers=headers)
   
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                print(title.encode(sys.stdout.encoding, errors='replace').decode())
        else:
            print("No posts found.")
    else:
        print("None")
