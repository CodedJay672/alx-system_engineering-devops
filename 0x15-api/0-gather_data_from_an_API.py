#1/usr/bin/python3
"""
python script that uses REST API to get data from a
domain.

"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "user/{}".format(
                        sys.argv[1])).json()
    tasks = reqests.get(url + "todos", params={"userid": sys.argv[1]}).json()
    completed = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
          user.get("name"), len(comleted), len(tasks)))
    for c in completed:
        print("\t {}".format(c))
