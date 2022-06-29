import logging
from datetime import datetime, timedelta

class Payment:   
    def __init__(self, employee_worked_hour_dict) -> dict:
        self.employee_worked_hours_dict = employee_worked_hour_dict     
        self.days_monday_friday = ["MO", "TU", "WE", "TH", "FR"]
        self.days_saturday_sunday = ["SA", "SU"]

    def sum_payment(self, start_time, end_time, values_dict) -> float:
        for values_dict_item in values_dict:
            sum_payment_value = 0
            start_time_values = datetime.strptime(values_dict_item["start"], '%H:%M')
            end_time_values = datetime.strptime(values_dict_item["end"], '%H:%M')

            time_0000 = datetime.strptime("00:00", '%H:%M')
            one_minute = timedelta(minutes=1)

            start_time_values -= one_minute

            if (end_time_values == time_0000):
                end_time_values = datetime.strptime("23:59", '%H:%M')

            if start_time >= start_time_values and end_time <= end_time_values:
                hours_worked = end_time - start_time
                payment = (int(hours_worked.seconds)/3600) * (int(values_dict_item["value"]))
                sum_payment_value += payment
                logging.debug(f"Start: {start_time}. End: {end_time}. Hours worked: {hours_worked}. Hour Value: {values_dict_item['value']}. Payment: {payment}. Payment Total: {sum_payment_value + self.employee_payment_total}")
                break
            elif start_time < end_time_values:
                hours_worked = end_time_values - start_time
                payment = (int(hours_worked.seconds)/3600) * (int(values_dict_item["value"]))
                sum_payment_value += payment
                logging.debug(f"Start: {start_time}. End: {end_time}. Hours worked: {hours_worked}. Hour Value: {values_dict_item['value']}. Payment: {payment}. Payment Total: {sum_payment_value + self.employee_payment_total}")
                start_time = end_time_values

        return sum_payment_value

    def calculate_payment(self, working_hours_values_monday_friday_dict, working_hours_values_saturday_sunday_dict):
        for employee in self.employee_worked_hours_dict:
            employee_days_dict = self.employee_worked_hours_dict[employee]
            self.employee_payment_total = 0
        
            for day in employee_days_dict:
                logging.debug(f"Calculating values from employee {employee} from day {day}.")
                day_dict = employee_days_dict[day]
                
                start_time = datetime.strptime(day_dict["start"], '%H:%M')
                end_time = datetime.strptime(day_dict["end"], '%H:%M')

                if day in self.days_monday_friday:
                    self.employee_payment_total += self.sum_payment(start_time, end_time, working_hours_values_monday_friday_dict)
                else:
                    self.employee_payment_total += self.sum_payment(start_time, end_time, working_hours_values_saturday_sunday_dict)

            print(f"The amount to pay {str.upper(employee)} is: {self.employee_payment_total} USD")
                    
        