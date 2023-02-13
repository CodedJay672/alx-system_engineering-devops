#!/usr/bin/python3
"""
python script that uses REST API to get data from a
domain.
script also exports dll ata obtained into a file in JSON format

"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    dictionary = {u.get("id"): [
        {"task": t.get("title"), "completed": t.get(
            "completed"), "username": u.get("username")}
        for t in requests.get(
            url + "todos", params={"userId": u.get("id")}).json()
        ]
        for u in user}

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(dictionary, json_file)
