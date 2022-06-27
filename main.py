#!python3

import json
from signal import raise_signal
import string
import re
from Payment import Payment

def read_json_file(json_file_name: string):
    try:
        json_file = open(json_file_name, "r")    
        return json.load(json_file)
    except:
        print (f"Error reading json file {json_file_name}")

def read_txt_file(txt_file_name: string):
    try:
        txt_file_content = open(txt_file_name, "r").read().splitlines() 

        return txt_file_content
    except:
        print (f"Error reading txt file {txt_file_name}")

def get_values_from_working_hours_file(file_name):
    working_hour_values = read_json_file(file_name)

    return working_hour_values

def get_values_from_employees_worked_hours_file(file_name):
    employees_hours_worked = read_txt_file(file_name)
    
    return employees_hours_worked

def get_working_hour_values_from_period(period, working_hour_values_file_name):

    working_hour_values_list = get_values_from_working_hours_file(working_hour_values_file_name)
    try:
        working_hour_values_from_period = working_hour_values_list[period]
        return working_hour_values_from_period
    except:
        print (f"Error getting working hour values from period: {period}")

def get_employees_worked_hours_dict(employees_hours_worked_file_name):
    
    employee_worked_hours_dict = {}
    worked_hours_regex = r"([0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2})"
    worked_days_regex = r"[a-zA-Z]{2}"

    employees_worked_hours_list = get_values_from_employees_worked_hours_file(employees_hours_worked_file_name)

    for employees_worked_hours_item in employees_worked_hours_list:
        
        worked_hours_dict = {}

        # Employee name
        employee_name = employees_worked_hours_item.partition("=")[0]
        print(employee_name)

        worked_info = employees_worked_hours_item.partition("=")[2]
        print(worked_info)

        # Worked days
        worked_days = re.findall(worked_days_regex, worked_info)

        # Worked hours
        worked_hours = re.findall(worked_hours_regex, worked_info)

        index = 0       
        while index < len(worked_days):
            worked_hours_dict[worked_days[index]] = json.loads(f"{{\"start\": \"{worked_hours[index][:5]}\", \"end\": \"{worked_hours[index][6:]}\"}}")
            index += 1

        employee_worked_hours_dict[employee_name] = worked_hours_dict

    return employee_worked_hours_dict

working_hour_values_file_name = "working_hour_values.json" 
employees_hours_worked_file_name = "input_employees_worked_hours.txt"

working_hours_values_monday_friday_dict = get_working_hour_values_from_period("monday-friday", working_hour_values_file_name)
working_hours_values_saturday_sunday_dict = get_working_hour_values_from_period("saturday-sunday", working_hour_values_file_name)

employee_worked_hours_dict = get_employees_worked_hours_dict(employees_hours_worked_file_name)

payment_obj = Payment(employee_worked_hours_dict)
payment_obj.calculate_payment(working_hours_values_monday_friday_dict, working_hours_values_saturday_sunday_dict)

