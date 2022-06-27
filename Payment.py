#!python3

class Payment:

    employee_worked_hours_dict = {}
    employees_payments = {}
    days_monday_friday = ["MO", "TU", "WE", "TH", "FR"]
    days_saturday_sunday = ["SA", "SU"]
    

    def __init__(self, employee_worked_hour_dict) -> dict:
        self.employee_worked_hours_dict = employee_worked_hour_dict

    def sum_payment(self, start_time, end_time, values_dict) -> float:
        from datetime import datetime

        employee_payment_total = 0

        for values_dict_item in values_dict:
            start_time_values = datetime.strptime(values_dict_item["start"], '%H:%M')
            end_time_values = datetime.strptime(values_dict_item["end"], '%H:%M')

            if start_time >= start_time_values and end_time <= end_time_values:
                hours_worked = end_time - start_time
                employee_payment_total += (int(hours_worked.seconds)/3600) * (int(values_dict_item["value"]))

        return employee_payment_total

    def calculate_payment(self, working_hours_values_monday_friday_dict, working_hours_values_saturday_sunday_dict):
        from datetime import datetime

        employee_payment_dict = {}
        for employee in self.employee_worked_hours_dict:
            print(employee)
            employee_days_dict = self.employee_worked_hours_dict[employee]
            print(employee_days_dict)
            employee_payment_total = 0
            for day in employee_days_dict:
                print(day)
                day_dict = employee_days_dict[day]
                
                start_time = datetime.strptime(day_dict["start"], '%H:%M')
                end_time = datetime.strptime(day_dict["end"], '%H:%M')

                if day in self.days_monday_friday:
                    employee_payment_total += self.sum_payment(start_time, end_time, working_hours_values_monday_friday_dict)
                    # for values_monday_friday in working_hours_values_monday_friday_dict:
                    #     start_time_values = datetime.strptime(values_monday_friday["start"], '%H:%M')
                    #     end_time_values = datetime.strptime(values_monday_friday["end"], '%H:%M')

                    #     if start_time >= start_time_values and end_time <= end_time_values:
                    #         hours_worked = end_time - start_time
                    #         employee_payment_total += (int(hours_worked.seconds)/3600) * (int(values_monday_friday["value"]))
                else:
                    employee_payment_total += self.sum_payment(start_time, end_time, working_hours_values_saturday_sunday_dict)
                    # for values_saturday_sunday in working_hours_values_saturday_sunday_dict:
                    #     start_time_values = datetime.strptime(values_saturday_sunday["start"], '%H:%M')
                    #     end_time_values = datetime.strptime(values_monday_friday["end"], '%H:%M')

                    #     if start_time >= start_time_values and end_time <= end_time_values:
                    #         hours_worked = end_time - start_time
                    #         employee_payment_total += (int(hours_worked.seconds)/3600) * (int(values_monday_friday["value"]))

                        #start_time_values = datetime.strptime(working_hours_values_monday_friday_dict[values_monday_friday], '%H:%M')
                        #end_time_values = datetime.strptime(working_hours_values_monday_friday_dict[values_monday_friday], '%H:%M')
            print(f"{employee}: USD {employee_payment_total}")
                    
        