#!/usr/bin/python3
"""
    get the id pased as argument
    and convert data into a csv file
"""
import csv
import requests
from sys import argv


api_user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
response = requests.get(api_user)
api_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
    argv[1])
response2 = requests.get(api_todos)
f = csv.writer(open("{}.csv".format(argv[1]), "w"))
for x in response2.json():
    f.writerow([x["userId"], response.json()[
        "username"], x["completed"], x["title"]])
