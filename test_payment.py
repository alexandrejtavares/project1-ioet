from Payment import Payment
from datetime import datetime

dic_days={}
dic_days = {
    "MO": {"start": "10:00", "end": "12:00"},
    "TU": {"start": "10:00", "end": "12:00"},
    "TH": {"start": "01:00", "end": "03:00"},
    "SA": {"start": "14:00", "end": "18:00"},
    "SU": {"start": "20:00", "end": "21:00"}}

employee_worked_hour_dict = {}
employee_worked_hour_dict["RENE"] = dic_days

payment = Payment(employee_worked_hour_dict)

working_hours_values_monday_friday_dict = [
        {"start": "00:01", "end": "09:00", "value": "25"},
        {"start": "09:01", "end": "18:00", "value": "15"},
        {"start": "18:01", "end": "00:00", "value": "20"}
    ]

working_hours_values_saturday_sunday_dict = [
        {"start": "00:01", "end": "09:00", "value": "30"},
        {"start": "09:01", "end": "18:00", "value": "20"},
        {"start": "18:01", "end": "00:00", "value": "25"}
    ]

def test_calculate_payment():
    assert payment.calculate_payment(working_hours_values_monday_friday_dict, working_hours_values_saturday_sunday_dict) == {"RENE": 215.0}

def test_sum_payment():
    assert payment.sum_payment(datetime.strptime("10:00", "%H:%M"), datetime.strptime("12:00", "%H:%M"), working_hours_values_saturday_sunday_dict) == 40.0
