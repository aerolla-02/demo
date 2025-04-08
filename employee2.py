from datetime import datetime

class Employee:
    def __init__(self, employee_id, employee_name, date_of_joining, salary, designation):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.date_of_joining = datetime.strptime(date_of_joining, "%Y-%m-%d")
        self.salary = salary
        self.designation = designation

    def apply_salary_hike(self):
        current_date = datetime.now()
        years_worked = (current_date - self.date_of_joining).days // 365
        
        if years_worked >= 5:
            self.salary = int(self.salary * 1.30)  # 30% hike
        elif years_worked >= 2:
            self.salary = int(self.salary * 1.05)  # 5% hike

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.employee_name}, DOJ: {self.date_of_joining.date()}, Salary: {self.salary}, Designation: {self.designation}"

# List of Employee objects
employees = [
    Employee(1, "John Doe", "2020-03-15", 50000, "Software Engineer"),
    Employee(2, "Jane Smith", "2018-06-20", 60000, "Senior Developer"),
    Employee(3, "Alice Johnson", "2023-01-10", 40000, "Junior Developer")
]

# Apply salary hike
for emp in employees:
    emp.apply_salary_hike()

# View employees
def view_employees():
    for emp in employees:
        print(emp)

view_employees()
 