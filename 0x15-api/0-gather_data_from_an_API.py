#!/usr/bin/python3
"""
    get the id pased as argument
    and get the info
    of that emplyeed
"""
import requests
from sys import argv


""" the user """
api_user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
response = requests.get(api_user)
""" the todo lists """
api_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
    argv[1])
response2 = requests.get(api_todo)
if response2.status_code == 200 & response.status_code == 200:
    """ print(response.json()) """
    emp_name = response.json()["name"]
    completed = 0
    todo = 0
    for i in response2.json():
        if i["completed"] is True:
            completed += 1
        todo += 1
    print(f"Employee {emp_name} is done with tasks({completed}/{todo})")
    list_todo = 0
    for f in response2.json():
        if f["completed"] is True:
            print("\t {}".format(response2.json()[list_todo]["title"]))
        list_todo += 1
