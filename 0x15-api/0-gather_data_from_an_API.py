#!/usr/bin/python3
"""
This Python script retrieves the progress of an employee's TODO list based on their ID
using a specified REST API.
"""
import requests
import sys

def fetch_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_info = requests.get(f'{base_url}users/{employee_id}').json()
    tasks = requests.get(f'{base_url}todos', params={'userId': employee_id}).json()

    # Filtering completed tasks
    tasks_done = [task["title"] for task in tasks if task['completed']]
    print(f"Employee {user_info.get('name')} is done with tasks({len(tasks_done)}/{len(tasks)})")
    
    # Printing completed tasks
    for task_title in tasks_done:
        print(f"\t {task_title}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        fetch_todo_progress(employee_id)
    else:
        print("Usage: script.py <employee_id>")

