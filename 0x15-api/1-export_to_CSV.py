#!/usr/bin/python3
'''This is a module'''

import csv
import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com'

    emp_req = '{}/users/{}'.format(url, id)
    res1 = requests.get(emp_req).json()
    username = res1.get('username')

    task_req = '{}/users/{}/todos'.format(url, id)
    res2 = requests.get(task_req).json()
    filename = '{}.csv'.format(id)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)

        for i in res2:
            userId = i.get('userId')
            status = i.get('completed')
            title = i.get('title')
            writer.writerow([userId, username, status, title])
