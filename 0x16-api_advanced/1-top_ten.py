#!/usr/bin/python3
'''This is a python module'''


def top_ten(subreddit):
    '''
    Args:
        subreddit: subreddit name
    prints:
        titles of the first 10 hot posts listed,
        or None for invalid subreddits
    '''
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    payload = {'limit': '10'}
    res = requests.get(url, headers=headers, params=payload,
                       allow_redirects=False)

    if res.status_code == 200:
        for i in res.json().get('data').get('children'):
            print(i.get('data').get('title'))
    else:
        print(None)
