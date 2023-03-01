import datetime
from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager
import unittest.mock as mock


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


def test_calculate_salary_and_send_email():
    rm = RelationsManager()
    e1 = Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                  birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1990, 10, 1))
    em = EmployeeManager(rm)
    email_sender_mock = mock.Mock()
    message = em.calculate_salary_and_send_email(e1, email_sender=email_sender_mock)
    expected_message = f"{e1.first_name} {e1.last_name} your salary: {em.calculate_salary(e1)} has been transferred " \
                       f"to you."
    email_sender_mock.send_email.assert_called_once_with(message, expected_message)

# tests passed
