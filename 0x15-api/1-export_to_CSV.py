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
user_dict = response.json()
api_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
    argv[1])
response2 = requests.get(api_todos)
todos_dict = response2.json()
count = 0

for x in response2.json():
    data = []
    a = [argv[1], user_dict["username"]]
    b = [todos_dict[count]["completed"], todos_dict[count]["title"]]
    c = a + b
    count += 1
    with open("{}.csv".format(argv[1]), 'a+') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(c)
