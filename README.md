# ACME - Employee Pay Calculation

## Introduction  

This program calculates the payment of employees based on worked hours inputted in a txt file named *input_employees_worked_hours.txt*, following the defined format, as example below:

EMPLOYEE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

The payment values table where we found the correspondent day and hour values was inputed into a json file named *working_hour_values.json* to avoid the need of code changes in case of  hour values changes.  

## Running Instructions  

First clone this repository as below:

- git clone https://github.com/alexandrejtavares/project1-ioet.git

After clone, open a Windows command promt or Linux/Unix shell with Python 3 installed and run the command below inside project directory:

- python main.py  

## Test Instructions  

The program uses the PyTest framework to test the modules.  

First install PyTest executing the command bellow:

- pip install pytest

Than, inside the project path execute the command:

- pytest -v

## Problem Description

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

**Monday - Friday**  
00:01 - 09:00 25 USD  
09:01 - 18:00 15 USD  
18:01 - 00:00 20 USD  

**Saturday and Sunday**  
00:01 - 09:00 30 USD  
09:01 - 18:00 20 USD  
18:01 - 00:00 25 USD  

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday  
TU: Tuesday  
WE: Wednesday  
TH: Thursday  
FR: Friday  
SA: Saturday  
SU: Sunday  

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

### Case 1 

**INPUT**
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

**OUTPUT:**
The amount to pay RENE is: 215 USD

### Case 2: 

**INPUT**
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

**OUTPUT:**
The amount to pay ASTRID is: 85 USD
