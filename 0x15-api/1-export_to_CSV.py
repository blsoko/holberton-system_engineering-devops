#!/usr/bin/python3
""" Export to csv file """
from sys import argv
import csv
import requests

if __name__ == "__main__":
    empName = ""
    employee_list = []
    doTask_list = []
    userid = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    for i in range(0, len(r.json())):
        if r.json()[i].get('userId', userid) is userid:
            doTask_list.append(r.json()[i].get('completed'))
            employee_list.append(r.json()[i].get('title'))
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    empName = r.json()[userid - 1].get('username')

    with open('{}.csv'.format(userid), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',',
                                     quoting=csv.QUOTE_ALL)
        for status, tittle in zip(doTask_list, employee_list):
            employee_writer.writerow([userid,
                                     empName, status,
                                     tittle])
