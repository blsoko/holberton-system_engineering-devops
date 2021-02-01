#!/usr/bin/python3
""" Gather data from HTTP Response """
import json
import requests
from sys import argv


if __name__ == "__main__":
    empName = ""
    totalTask = 0
    doneTask = 0
    employee_list = []
    userid = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    for i in range(0, len(r.json())):
        if r.json()[i].get('userId', userid) is userid:
            totalTask += 1
            if r.json()[i].get('completed') is True:
                employee_list.append(r.json()[i].get('title'))
                doneTask += 1
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    empName = r.json()[userid - 1].get('name')
    print('Employee {} is done with tasks({}/{}):'
          .format(empName, doneTask, totalTask))
    for tittle in employee_list:
        print("\t {}".format(tittle))
