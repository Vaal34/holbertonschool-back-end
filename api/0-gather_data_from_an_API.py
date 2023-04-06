#!/usr/bin/python3
""" using this REST API """


import requests
from sys import argv

if __name__ == '__main__':
    """ Check """

    id = argv[1]
    id = int(id)

    # variable qui stocke url parce que c'est trop long pour pep8
    url_user_api = f"https://jsonplaceholder.typicode.com/users/{id}"

    user = requests.get(url_user_api).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    task = 0
    task_valid = 0

    for userid in todo:
        if userid['userId'] == id:
            task += 1
            if userid['completed']:
                task_valid += 1

    print(f"Employee {user['name']} is done with tasks({task_valid}/{task}):")

    for title in todo:
        if title['completed'] and title['userId'] == id:
            print(f"\t {title['title']}")
