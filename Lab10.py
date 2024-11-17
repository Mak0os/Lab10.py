# Program Name: Lab10.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab10
# Due Date: 10/20/2024
# Purpose: This program modifies the Worker class to throw exceptions for invalid input in getter/setter methods.

class Worker:
    def __init__(self):
        self.employee_number = None
        self.office_number = None
        self.name = {'first': '', 'last': ''}
        self.birthdate = {'day': 0, 'month': 0, 'year': 0}
        self.total_hours_worked = 0
        self.total_overtime_hours = 0
        self.hourly_salary = 0.0
        self.overtime_salary = 0.0

    def get_employee_number(self):
        return self.employee_number

    def set_employee_number(self, x):
        if not isinstance(x, int):
            raise TypeError("Employee number must be an integer.")
        self.employee_number = x

    def get_office_number(self):
        return self.office_number

    def set_office_number(self, x):
        if x < 100 or x > 500:
            raise ValueError("Office number must be between 100 and 500.")
        self.office_number = x

    def get_name(self):
        return f"{self.name['first']} {self.name['last']}"

    def set_name(self, first_name, last_name):
        def sanitize_name(name):
            return name.replace('_', '').replace('.', '').replace('-', '')

        if not first_name or not last_name:
            raise ValueError("First and last names cannot be empty.")
        self.name['first'] = sanitize_name(first_name)
        self.name['last'] = sanitize_name(last_name)

    def set_birthdate(self, d, m, y):
        if m < 1 or m > 12:
            raise ValueError("Month must be between 1 and 12.")
        if d < 1 or d > 31:
            raise ValueError("Day must be between 1 and 31.")
        self.birthdate['day'] = d
        self.birthdate['month'] = m
        self.birthdate['year'] = y

    def get_hours_worked(self):
        return self.total_hours_worked

    def add_hours(self, x):
        if x < 0:
            raise ValueError("Number of hours added cannot be less than 0.")
        if x > 9:
            self.total_hours_worked += 9
            self.total_overtime_hours += (x - 9)
        else:
            self.total_hours_worked += x

    def get_hours_overtime(self):
        return self.total_overtime_hours

    def set_hourly_salary(self, x):
        if x < 0:
            raise ValueError("Hourly salary cannot be negative.")
        self.hourly_salary = x

    def set_overtime_salary(self, x):
        if x < 0:
            raise ValueError("Overtime salary cannot be negative.")
        self.overtime_salary = x

    def get_hourly_salary(self):
        return self.hourly_salary

    def get_overtime_salary(self):
        return self.overtime_salary

    def get_pay(self):
        return (self.total_hours_worked * self.hourly_salary) + (self.total_overtime_hours * self.overtime_salary)

# Example usage for testing
if __name__ == "__main__":
    worker = Worker()
    try:
        worker.set_employee_number(12345)
        worker.set_office_number(200)
        worker.set_name("Jane", "Doe")
        worker.set_birthdate(12, 5, 1990)
        worker.add_hours(10)
        worker.set_hourly_salary(25)
        worker.set_overtime_salary(35)
        print("Employee Info:")
        print(f"Number: {worker.get_employee_number()}, Name: {worker.get_name()}, Total Pay: ${worker.get_pay()}")
    except Exception as e:
        print(f"Error: {e}")
