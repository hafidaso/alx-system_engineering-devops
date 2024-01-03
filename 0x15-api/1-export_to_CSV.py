#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

# Disable warnings (not recommended for production code)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user and todo data
    user = requests.get(f"{url}users/{user_id}", verify=False).json()
    username = user.get("username")
    todos = requests.get(f"{url}todos", params={"userId": user_id}, verify=False).json()

    # Write data to CSV
    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([user_id, username, t.get("completed"), t.get("title")])

