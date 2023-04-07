#!/usr/bin/python3
""" using this REST API """


import requests
import json
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

    USER_ID = user['id']
    USERNAME = user['username']
    new_dict = {}
    list = []

    for data in todo:
        if data['userId'] == id:
            new_dict = dict(task=data['title'],
                            completed=data['completed'], username=USERNAME)
            list.append(new_dict)

    jsonfile = {f"{USER_ID}": list}

    print(jsonfile)
    with open(f"{USER_ID}.json", 'w') as new_file:
        json.dump(jsonfile, new_file)
