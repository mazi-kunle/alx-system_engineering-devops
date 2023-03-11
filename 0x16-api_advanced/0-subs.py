#!/usr/bin/python3
'''A python module'''


def number_of_subscribers(subreddit):
    '''
    Args:
        subreddit: subreddit name
    Return:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid
    '''
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return(res.json().get('data').get('subscribers'))
    return 0
