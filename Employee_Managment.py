import mysql.connector
imp =  mysql.connector.connect(user='Your name', password='Your password',
                              host='127.0.0.1',
                              database='emp')
def check_employee(employee_id):
    sql = 'Select * from employees where id=%s'
    cursor = imp.cursor(buffered=True)
    data = (employee_id,)
    cursor.execute(sql,data)
    employee = cursor.fetchone()
    cursor.close()
    return employee is not None

def add_employee():
    ID = input('Enter Employee ID')
    if check_employee(ID):
        print("Employee already exists. Please try with new Id.")
        return
    else:
        name = input('Enter Name -')
        designation = input('Enter Role -')
        salary = input('Enter Salary -')
        sql = 'insert into employees(ID,name,designation,salary) Values (%s,%s,%s,%s)'
        data = (ID,name,designation,salary)
        cursor = imp.cursor()
        try:
            cursor.execute(sql,data)
            imp.commit()
            print('Details added successfully')
        except mysql.connector.errors as error:
            print('Error-',error)
            imp.rollback()
        finally:
            cursor.close()
def remove_employee():
    ID = input('Enter Employee ID-')
    if not check_employee(ID):
        print('Employee does not exist. Please try again')
        return
    else:
        sql = 'delete from employees where id=%s'
        data = (ID,)
        cursor  = imp.cursor()
    try:
        cursor.execute(sql,data)
        imp.commit()
        print('Employee Removed Successfully')
    except mysql.connector.errors as error:
        print('Error-',error)
        imp.rollback()
    finally:
        cursor.close()

def promote_employee():
    ID = input('Enter Employee ID-')
    if not check_employee(ID):
        print('Employee does not exist. Please try again')
        return
    else:
        try:
            Amount = float(input('Enter Increment Amount-'))
            selection = 'select * from employees where id=%s'
            data = (ID,)
            cursor = imp.cursor()
            cursor.execute(selection,data)

            current_salary = cursor.fetchone()[0]
            new_salary = current_salary+Amount

            sql = 'update employees set salary=%s where id=%s'
            data1 = (sql,new_salary)
            cursor.execute(sql,data1)
            imp.commit()
            print('Amount incremented Successfully')
        except mysql.connector.errors as error:
            print('Error-',error)
            imp.rollback()
        finally:
            cursor.close()
def display_emp():
    try:
        sql = 'select * from employees'
        cursor = imp.cursor()
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print('ID:',employee[0])
            print('Name:',employee[1])
            print('Designation:',employee[2])
            print('Salary:',employee[3])
            print('=================================*===============================')

    except mysql.connector.errors as error:
        print('Error-',error)
    finally:
        cursor.close()
while True:
    print("\nWelcome to Employee Management Record")
    print("Press:")
    print("1 to Add Employee")
    print("2 to Remove Employee")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")

    a = input('Enter your choice -')
    if a==1:
        add_employee()
    if a==2:
        remove_employee()
    if a==3:
        promote_employee()
    if a==4:
        display_emp()
    if a==5:
        break
    else:
        print('Choice is Invalid')

