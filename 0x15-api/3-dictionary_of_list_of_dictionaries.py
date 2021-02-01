#!/usr/bin/python3
""" Export all to json file """
from sys import argv
import json
import requests

if __name__ == "__main__":
    subdict = {}
    mylist = []
    jsondict = {}
    nameUsr = requests.get('https://jsonplaceholder.typicode.com/users')
    for i in range(0, len(nameUsr.json())):
        idUsr = nameUsr.json()[i].get('id')
        todosUsr = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(idUsr))
        for i in range(0, len(todosUsr.json())):
            status = todosUsr.json()[i].get('completed')
            title = todosUsr.json()[i].get('title')
            username = nameUsr.json()[idUsr - 1].get('username')
            subdict = {
                "task": title,
                "completed": status,
                "username": username}
            mylist.append(subdict)
        jsondict.update({idUsr: mylist})
        mylist = []

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(jsondict, outfile)
