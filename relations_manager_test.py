from datetime import date
from employee_manager import EmployeeManager
from employee import Employee
from relations_manager import RelationsManager


def test_john_doe_is_leader():
    rm = RelationsManager()
    john = Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                    birth_date=date(1970, 1, 31), hire_date=date(1990, 10, 1))
    assert rm.is_leader(john) == True


def test_john_doe_team_members():
    rm = RelationsManager()
    john = Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                    birth_date=date(1970, 1, 31), hire_date=date(1990, 10, 1))
    team_members = rm.get_team_members(john)
    all_employees = rm.get_all_employees()
    assert len(team_members) == 2
    assert any(emp.first_name == "Myrta" and emp.last_name == "Torkelson" and emp.id in team_members for emp in
               all_employees)
    assert any(emp.first_name == "Jettie" and emp.last_name == "Lynch" and emp.id in team_members for emp in
               all_employees)


def test_tomas_andre_not_on_team():
    rm = RelationsManager()
    john = Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                    birth_date=date(1970, 1, 31), hire_date=date(1990, 10, 1))
    team_members = rm.get_team_members(john)
    all_employees = rm.get_all_employees()
    assert not any(emp.first_name == "Tomas" and emp.last_name == "Andre" and emp.id in team_members for emp in
                   all_employees)


def test_gretchen_watford_base_salary():
    rm = RelationsManager()
    all_employees = rm.get_all_employees()
    assert any(emp.first_name == "Gretchen" and emp.last_name == "Watford" and emp.base_salary == 4000 for emp in
               all_employees)
