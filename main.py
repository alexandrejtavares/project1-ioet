#!python3

import json
from signal import raise_signal
import sys

def get_values_from_working_hour_values_file():
    file_name = "working_hour_values.json" 

    working_hour_values_file = open(file_name, "r")    
    working_hour_values = json.load(working_hour_values_file)

    return working_hour_values

    
working_hour_values = get_values_from_working_hour_values_file()
try:
    working_hour_values_monday_friday = working_hour_values["monday-friday"]
    working_hour_values_saturday = working_hour_values["saturday-sunday"]
except Exception as e:
    print (f"Error on getting values from working hour: {e}")
    sys.exit(1)

print (working_hour_values_saturday)
