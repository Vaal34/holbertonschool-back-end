#!/usr/bin/python3
""" using this REST API """


import requests
from sys import argv

id = argv[1]
id = int(id)

user = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}").json()
todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

task = 0
task_valid = 0

for userid in todo:
    if userid['userId'] == id:
        task += 1
        if userid['completed']:
            task_valid += 1

print(f"Employee {user['name']} is done with tasks({task_valid}/{task})")

for title in todo:
    if title['completed'] and title['userId'] == id:
        print(title['title'])
