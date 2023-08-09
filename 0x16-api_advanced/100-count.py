#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles
, and prints a sorted count of given keywords"""

import requests

def count_words(subreddit, word_list, after=None, keyword_count={}):
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    title_lower = title.lower()
                    if keyword_lower in title_lower:
                        if keyword_lower in keyword_count:
                            keyword_count[keyword_lower] += 1
                        else:
                            keyword_count[keyword_lower] = 1
            new_after = data['data']['after']
            if new_after is not None:
                count_words(subreddit, word_list, new_after, keyword_count)
            else:
                sorted_keywords = sorted(keyword_count.items(), key=lambda x: (-x[1], x[0]))
                for keyword, count in sorted_keywords:
                    print("{}: {}".format(keyword, count))
        else:
            print("No results found.")
    else:
        print("No results found.")
