import datetime
from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager


def test_calculate_salary_for_non_leader_employee():
    rm = RelationsManager()
    em = EmployeeManager(rm)
    employee = Employee(id=2, first_name="Jane", last_name="Doe", base_salary=1000,
                        birth_date=datetime.date(1972, 10, 14), hire_date=datetime.date(1998, 10, 10))
    actual_salary = em.calculate_salary(employee)
    assert actual_salary == 3500
