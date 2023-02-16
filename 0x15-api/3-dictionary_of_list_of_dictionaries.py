#!/usr/bin/python3
'''This is a module'''


import json
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'

    res1 = requests.get(url).json()

    filename = 'todo_all_employees.json'
    dict_ = {}

    for data in res1:
        username = data.get('username')
        id = str(data.get('id'))
        dict_[id] = []
        a = '{}/{}/todos'.format(url, id)

        res2 = requests.get(a).json()

        for task in res2:
            value = {
                        "username": username,
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                    }
            dict_.get(id).append(value)

    # write to json file
    with open(filename, 'w') as f:
        json.dump(dict_, f)
