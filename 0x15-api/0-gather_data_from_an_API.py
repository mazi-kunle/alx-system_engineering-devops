#!/usr/bin/python3
'''This is a module'''

import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com'

    emp_req = '{}/users/{}'.format(url, id)
    res1 = requests.get(emp_req).json()
    emp_name = res1.get('name')

    task_req = '{}/users/{}/todos'.format(url, id)
    res2 = requests.get(task_req).json()
    tasks = len(res2)
    completed_tasks = list(filter(lambda a: a.get('completed'), res2))

    print('Employee {} is done with tasks({}/{})'.
          format(emp_name, len(completed_tasks), tasks))

    for i in completed_tasks:
        print('\t {}'.format(i.get('title')))
