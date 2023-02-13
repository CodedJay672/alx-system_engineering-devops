#!/usr/bin/python3
"""
python script that uses REST API to get data from a
domain.
script also exports data obtained into a file in JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    dictionary = {sys.argv[1]: [{"task": t.get("title"), "completed": t.get(
        "completed"), "username": username} for t in tasks]}

    with open("{}.json".format(sys.argv[1]), "w") as json_file:
        json.dump(dictionary, json_file)
