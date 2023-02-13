#!/usr/bin/python3
"""
python script that uses REST API to get data from a
domain.

"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csv_file:
        my_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [my_writer.writerow(
            [sys.argv[1], username, t.get("completed"), t.get("title")]
         ) for t in tasks]
