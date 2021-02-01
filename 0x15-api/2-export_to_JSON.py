#!/usr/bin/python3
""" Export to json file """
from sys import argv
import json
import requests

if __name__ == "__main__":
    empusrName = ""
    employee_list = []
    doTask_list = []
    userid = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    for i in range(0, len(r.json())):
        if r.json()[i].get('userId', userid) is userid:
            doTask_list.append(r.json()[i].get('completed'))
            employee_list.append(r.json()[i].get('title'))
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    empusrName = r.json()[userid - 1].get('username')

    mylista = []
    mydict = {}
    for status, tittle in zip(doTask_list, employee_list):
        mydict = {"task": tittle, "completed": status, "username": empusrName}
        mylista.append(mydict)

    jsondict = {userid: mylista}
    with open('{}.json'.format(userid), 'w') as outfile:
        json.dump(jsondict, outfile)
