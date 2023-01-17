#!/usr/bin/python3

"""Using this:

REST API(https://jsonplaceholder.typicode.com/),
for a given employee ID,
returns information about his/her TODO list progress.
"""

import sys
import requests


def get_todos(emp_id:int):
    """Fetches data from a given API endpoint.

    Keyword arguments:
    emp_id -- employee id parameter (integer)
    """
    url1 = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    #Users URL
    userRequest = requests.get(url1)
    userdata = userRequest.json()
    username = userdata["name"]
    userId = userdata["id"]

    url = "https://jsonplaceholder.typicode.com/todos/"
    #todos URL
    todosRequest = requests.get(url)
    todosData = todosRequest.json()
    todos = []
    total = 0
    completed = 0

    for todo in todosData:
        if todo["userId"] == userId:
            total += 1
            if todo["completed"] is True:
                completed += 1
                todos.append(todo["title"])

    print(f'Employee {username} is done with tasks({completed}/{total}:')
    for task in todos:
        print(f'\t {task}')


if __name__ == "__main__":

    get_todos(sys.argv[1])
