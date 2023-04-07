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

USER_ID = user['id']
USERNAME = user['username']

with open('USER_ID.csv', 'w') as newfile:
    
    for data_task in todo:
        if data_task['userId'] == id:
            newfile.write(f"\"{USER_ID}\",\"{USERNAME}\",")
            newfile.write(f"\"{data_task['completed']}\",\"{data_task['title']}\"" + "\n")
