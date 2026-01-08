
def total_tasks_completed(employee_list: list) -> int:
    return sum(employee['tasks_completed'] for employee in employee_list)

def efficiency_ratio(employee):
    return employee['tasks_completed'] / employee['hours_worked']
    
def most_efficient_employee(employee_list: list) -> int:
    return max(
        employee_list, 
        key=lambda x: (efficiency_ratio(x), x['tasks_completed']), 
    )['employee_id']

def sort_by_hours_worked(employee_list: list) -> list:
    sorted_employees = sorted(
        employee_list,
        key=lambda x: (x['hours_worked'], x['tasks_completed']),
        reverse = True
    )
    return list(map(lambda x: x['employee_id'], sorted_employees))

def productive_team_members(employee_list: list) -> list:
    return [
        employee['employee_id'] 
        for employee in employee_list 
        if employee['tasks_completed'] >= 20
    ]


def process_employees(employee_list: list, request: str):
    """
    Process the employee list as per the request.
    
    Args:
        employee_list (list[dict]): List of dictionaries with the keys
            "employee_id", "tasks_completed", and "hours_worked".
        request (str): One of the following options:
            - 'total_tasks_completed'
            - 'most_efficient_employee'
            - 'sort_by_hours_worked'
            - 'productive_team_members'.
        
    Returns:
        The output corresponding to the request.
    """
    
    if request == 'total_tasks_completed':
        return total_tasks_completed(employee_list)
    elif request == 'most_efficient_employee':
        return most_efficient_employee(employee_list)
    elif request == 'sort_by_hours_worked':
        return sort_by_hours_worked(employee_list)
    elif request == 'productive_team_members':
        return productive_team_members(employee_list)
    
#    #Another Method:



# def process_employees(employee_list: list, request: str):
#     """
#     Process the employee list as per the request.
    
#     Args:
#         employee_list (list[dict]): List of dictionaries with the keys
#             "employee_id", "tasks_completed", and "hours_worked".
#         request (str): One of the following options:
#             - 'total_tasks_completed'
#             - 'most_efficient_employee'
#             - 'sort_by_hours_worked'
#             - 'productive_team_members'.
        
#     Returns:
#         The output corresponding to the request.
#     """
#     if request=='total_tasks_completed':
#         return sum(i["tasks_completed"] for i in employee_list)
#     if request=='most_efficient_employee':
#         max_dixt = max(employee_list, key=lambda i: i["tasks_completed"]/i['hours_worked'])
#         return max_dixt["employee_id"]
#     if request=='sort_by_hours_worked':
#         sorted_list=sorted(employee_list,key=lambda i:(i["hours_worked"],i["tasks_completed"]),reverse = True)
#         return [ i["employee_id"] for i in sorted_list]
#     if request=='productive_team_members':
#         prod_list=list(filter(lambda i: i["tasks_completed"]>=20,employee_list))
#         return [i["employee_id"] for i in prod_list]

# Employee Task Analysis
# Given a list of dictionaries representing employees where each dictionary contains the keys employee_id, tasks_completed, and hours_worked, write a function that does the following based on the given task:

# total_tasks_completed: Compute the total number of tasks completed by all employees combined.
# most_efficient_employee: Determine the id of the employee with the highest ratio of tasks_completed to hours_worked. If there are ties, break by the highest number of tasks completed.
# sort_by_hours_worked: Get the list of employee ids sorted by the number of hours worked from the highest to the lowest and break ties using the highest number of tasks completed.
# productive_team_members: Filter and return a list of employee ids of employees who have completed 20 or more tasks in the order that they are present in the employee list.
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# employee_list = [
#     {'employee_id': 1, 'tasks_completed': 30, 'hours_worked': 40},
#     {'employee_id': 2, 'tasks_completed': 60, 'hours_worked': 90},
#     {'employee_id': 3, 'tasks_completed': 60, 'hours_worked': 100},
#     {'employee_id': 4, 'tasks_completed': 50, 'hours_worked': 100},
#     {'employee_id': 5, 'tasks_completed': 10, 'hours_worked': 30},
# ]
# total_tasks_completed -> 30+60+60+50+10 = 210
# most_efficient_employee
# Employee 1 efficiency = 30/40 = 0.75
# Employee 2 efficiency = 60/90 = 0.66
# Employee 3 efficiency = 60/100 = 0.60
# Employee 4 efficiency = 50/100 = 0.50
# Employee 4 efficiency = 10/30 = 0.33
# Thus Employee 1 is most efficient
# sort_by_hours_worked -> [3, 4, 2, 1, 5] (3 and 4 has more number of hours worked but 3 has completed most tasks)
# productive_team_members -> [1, 2, 3, 4] (5 has completed less than 20 tasks, thus not included.)

