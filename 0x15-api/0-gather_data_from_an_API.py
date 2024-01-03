import requests
import sys

def get_employee_todo_list_progress(employee_id):
    # API endpoints
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetching user data
    user_response = requests.get(users_url)
    user_data = user_response.json()

    # Fetching todo list data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculating progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    # Displaying output
    print(f"Employee {user_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID.")
    else:
        print("Employee ID not provided. Usage: python script.py <employee_id>")

