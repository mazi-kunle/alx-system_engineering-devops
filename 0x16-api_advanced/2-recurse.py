#!/usr/bin/python3
'''This is a module'''


after = None


def recurse(subreddit, hotlist=[]):
    '''
    Args:
        subreddit: subreddit name
    Returns:
        list containining the titles of all 10 hot
        articles for a given subreddit,
        or None for invalid subreddits
    '''
    import requests

    global after
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    payload = {'after': after}
    res = requests.get(url, headers=headers, params=payload,
                       allow_redirects=False)
    if res.status_code == 200:
        next_ = res.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hotlist)

        for i in res.json().get('data').get('children'):
            hotlist.append(i.get('data').get('title'))

        return hotlist
    return None
