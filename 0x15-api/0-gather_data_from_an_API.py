#!/usr/bin/python3

import urllib.request
import json
import sys
"""
The above module enables me to fetch data from a url
parse it as a JSON format before using it

"""


def employee_id_info(employee_id):

    # endpoints for fetching data
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'''
    https://jsonplaceholder.typicode.com/todos?userId={employee_id}
    '''

    # fetch user data
    with urllib.request.urlopen(user_url) as response:
        user_data = response.read().decode('utf-8')
        user = json.loads(user_data)

    # fetch todo data
    with urllib.request.urlopen(todo_url) as response:
        todo_data = response.read().decode('utf-8')
        todos = json.loads(todo_data)

    # process and display the result in the format specified
    employee_name = user.get("name")
    completed_tasks = [
            todo["title"] for todo in todos if todo.get("completed")
            ]
    total_tasks = len(todos)

    print(f"""
    Employee {employee_name} is done with
    tasks({len(completed_tasks)}/{total_tasks}):
    """)
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    # Ensure the employee id is been passed as an argument
    employee_id = sys.argv[1]

    employee_id_info(employee_id)
