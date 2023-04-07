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
    my_list = []
    jsonfile = {}

    for employee in user:
        USER_ID = employee['id']
        USERNAME = employee['username']
        my_list = []
        for data in todo:
            if USER_ID == data['userId']:
                new_dict = dict(username=USERNAME, task=data['title'],
                                completed=data['completed'])
                my_list.append(new_dict)
        jsonfile[USER_ID] = my_list

    with open("todo_all_employees.json", 'w') as new_file:
        json.dump(jsonfile, new_file)
