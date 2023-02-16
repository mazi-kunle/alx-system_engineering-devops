#!/usr/bin/python3
'''This is a module'''


import json
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    id = argv[1]

    emp_req = '{}/users/{}'.format(url, id)
    res1 = requests.get(emp_req).json()

    task_req = '{}/users/{}/todos'.format(url, id)
    res2 = requests.get(task_req).json()

    filename = '{}.json'.format(id)
    dict_ = {str(id): []}
    username = res1.get('username')

    for task in res2:
        value = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                }
        dict_.get(str(id)).append(value)

    # write to json file
    with open(filename, 'w') as f:
        json.dump(dict_, f)

    dict_.get(str(id)).append(value)
