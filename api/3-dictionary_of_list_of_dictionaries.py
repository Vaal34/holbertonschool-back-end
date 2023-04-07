#!/usr/bin/python3
""" using this REST API """

import json
import requests
from sys import argv

if __name__ == '__main__':
    """ Check """

    # variable qui stocke url parce que c'est trop long pour pep8
    url_user_api = f"https://jsonplaceholder.typicode.com/users/"

    user = requests.get(url_user_api).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    new_dict = {}
    list = []
    final_dict = {}
    jsonfile = {}

    for employee in user:
        USER_ID = employee['id']
        USERNAME = employee['username']
        for data in todo:
            if USER_ID == data['id']:
                new_dict = dict(username=USERNAME, task=data['title'],
                                completed=data['completed'])
                list.append(new_dict)
        jsonfile[USER_ID] = list

    print(jsonfile)

    with open(f"{USER_ID}.json", 'w') as new_file:
        json.dump(jsonfile, new_file)
