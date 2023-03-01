from datetime import date
from employee_manager import EmployeeManager
from employee import Employee
from relations_manager import RelationsManager


def test_john_doe_is_leader():
    rm = RelationsManager()
    john = Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                    birth_date=date(1970, 1, 31), hire_date=date(1990, 10, 1))
    assert rm.is_leader(john) == True
