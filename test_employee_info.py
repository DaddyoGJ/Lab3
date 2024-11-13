import employee_info as employee
from employee_info import employee_data as employeedata

def test_get_employees_by_age_range():
    upper = 33
    lower = 29
    expected = [employeedata[0], employeedata[4]]
    result = employee.get_employees_by_age_range(lower, upper)

    assert (result == expected)

def test_calculate_average_salary():
    expected = 60166.67 #better to round it to 2d.p & should be exact else fail
    result = employee.calculate_average_salary()

    assert (result == expected)

def test_employees_by_dept():
    targetDept = "Sales"
    expected = [employeedata[0], employeedata[5]]
    result = employee.get_employees_by_dept(targetDept)

    assert (result == expected)