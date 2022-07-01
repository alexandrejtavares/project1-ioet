#!python3

import json
import logging
from Payment import Payment
import re

def read_json_file(json_file_name: str):
    try:
        json_file = open(json_file_name, "r")    
        return json.load(json_file)
    except:
        logging.critical("Error reading json file {json_file_name}")

def read_txt_file(txt_file_name: str):
    try:
        txt_file_content = open(txt_file_name, "r").read().splitlines() 
        return txt_file_content
    except:
        logging.critical(f"Error reading txt file {txt_file_name}")

def get_values_from_working_hours_file(file_name):
    working_hour_values = read_json_file(file_name)
    logging.debug(f"Reading values from working hours file: {file_name}")
    return working_hour_values

def get_values_from_employees_worked_hours_file(file_name):
    employees_hours_worked = read_txt_file(file_name)
    
    return employees_hours_worked

def get_working_hour_values_from_period(period, working_hour_values_list):   
    try:
        working_hour_values_from_period = working_hour_values_list[period]
        return working_hour_values_from_period
    except:
        logging.critical(f"Error getting working hour values from period: {period}.")

def get_employees_worked_hours_dict(employees_worked_hours_list):    
    employee_worked_hours_dict = {}
    worked_hours_regex = r"([0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2})"
    worked_days_regex = r"[a-zA-Z]{2}"

    for employees_worked_hours_item in employees_worked_hours_list:
        worked_hours_dict = {}

        # Employee name
        employee_name = employees_worked_hours_item.partition("=")[0]     
        worked_info = employees_worked_hours_item.partition("=")[2]

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

log_level = getattr(logging, "INFO", None) # CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=log_level)

working_hour_values_file_name = "working_hour_values.json" 
employees_hours_worked_file_name = "input_employees_worked_hours.txt"

# Read JSON file 
working_hour_values_list = get_values_from_working_hours_file(working_hour_values_file_name)

# Get the values of worked hours of week and weekend as dicts
working_hours_values_monday_friday_dict = get_working_hour_values_from_period("monday-friday", working_hour_values_list)
working_hours_values_saturday_sunday_dict = get_working_hour_values_from_period("saturday-sunday", working_hour_values_list)

# Read employees worked hours input file
employees_worked_hours_list = get_values_from_employees_worked_hours_file(employees_hours_worked_file_name)

# Get the total hours worked by an employee as dict
employee_worked_hours_dict = get_employees_worked_hours_dict(employees_worked_hours_list)

payment_obj = Payment(employee_worked_hours_dict)

dic_payment = payment_obj.calculate_payment(working_hours_values_monday_friday_dict, working_hours_values_saturday_sunday_dict)

for item in dic_payment:
    print(f"The amount to pay {item} is: {dic_payment[item]} USD")

#"The amount to pay {str.upper(employee)} is: {self.employee_payment_total} USD\n"