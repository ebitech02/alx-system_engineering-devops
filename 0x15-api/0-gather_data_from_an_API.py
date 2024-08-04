import json
import sys
from urllib.request import urlopen

def get_employee_id_todo_list(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        with urlopen(user_url) as response:
            user_data = response.read()
        with urlopen(todo_url) as response:
            todo_data = response.read()

            user = json.loads(user_data)
            todo = json.loads(todo_data)

            employee_name = user.get('name')
            completed_tasks = [task for task in todo if task.get('completed')]
            number_of_task_done = len(completed_tasks)
            total_tasks = len(todo)

            print(f"Employee {employee_name} is done with tasks({number_of_task_done}/{total_tasks}):")
            for task in completed_tasks:
                print(f"\t {task.get('title')}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
   if len(sys.argv) != 2:
       print("Usage: python3 script.py <employee_id>")
       sys.exit(1)
