#create a table called employees, employee ID, employee name, date of joining,salary, designation
#create a class employee, create 5 objects for this class write a loop that all this should be converted into table format should be added for the table
# create a table called employees, employee ID, employee name, date of joining,salary should be private, designation who ever has been in company for 2 years  5% hike and 5 years 30% hike,use only python
# write a decorator program to print hello world before and after executing a program
# write a list program to remove duplicate without type casting and not taking another list
#password encription
import sqlite3
conn=sqlite3.connect("employee.db")
cursor= conn.cursor()
# cursor.execute(''' create table employees (emp_id number(3) primary key, emp_name varchar(32) not null, DOJ date, salary number(8,2) not null, designation varchar(32) not null);''')

class employee:
    def __init__(self, id, name, doj, salary, designation):
        self.emp_id= id
        self.emp_name= name
        self.DOJ= doj
        self.salary=salary
        self.designation = designation
#    salary
employee1= employee(123, "john", "12-02-2018", 180000, "python dev")
employee2= employee(143, "suresh", "11-03-2021", 125000, "python dev")
employee3= employee(153, "mani", "6-4-2017", 245000,"C++ dev")
employee4= employee(163, "gadha", "12-10-2020", 95000, ".net dev")
employee5= employee(133, "danial", "23-12-2023", 70000,"java dev")
list= (employee1, employee2, employee3, employee4, employee5)
for i in list:
    print(i.emp_name, i.emp_id, i.DOJ, i.salary, i.designation)

    cursor.execute(f'''insert into employees (emp_id, emp_name, DOJ, designation, salary) values({i.emp_id},'{i.emp_name}','{i.DOJ}', {i.salary},'{i.designation}' );''')
conn.commit()








