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


def test_team_leader_salary_calculation():
    rm = RelationsManager()
    e1 = Employee(id=4, first_name="Gretchen", last_name="Watford", base_salary=2000,
                  birth_date=datetime.date(1985, 8, 22), hire_date=datetime.date(2008, 10, 10))
    em = EmployeeManager(rm)
    assert em.calculate_salary(e1) == 4100
