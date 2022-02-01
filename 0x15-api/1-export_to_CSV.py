#!/usr/bin/python3
"""
    get the id pased as argument
    and convert data into a csv file
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    api_user = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(api_user)
    api_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])
    response2 = requests.get(api_todos)
    a = [argv[1], response.json()["username"]]
    for x in response2.json():
        b = [x["completed"], x["title"]]
        c = a + b
        with open("{}.csv".format(argv[1]), 'a+') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(c)
