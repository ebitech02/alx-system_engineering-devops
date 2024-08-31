#!/usr/bin/python3

import json
import sys
import urllib.request
"""
Urllib.request: used to fetch data
Json: format data
Sys: to fetch and pass system arguments

"""


def employee_id_info(employee_id):
    """
    Description: Gets the employee id and formats the data received

    Args:
        Employee_id (int): Employee id.

    Returns:
        String: String of data.

    """

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
