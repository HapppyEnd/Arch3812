"""Переписать код в соответствии с Single Responsibility Principle.
​"""


class Employee:
    """class Employee."""

    def __init__(self, name: str, dob: str) -> None:
        self.name = name
        self.dob = dob

    def get_emp_info(self) -> str:
        """Get info about employee."""
        return f'name - {self.name} , dob - {self.dob}'

    def __str__(self) -> str:
        return self.name


class Account:
    """Class Account."""

    def __init__(self) -> None:
        self.employee = []

    def calculate_net_salary(self, base_salary: int) -> int:
        """Calculate salary."""
        return base_salary - int(base_salary * 0.25)


salary = Account()
salary.employee.append([Employee('Ann', '01.01.1987'),
                       salary.calculate_net_salary(500)])
salary.employee.append([Employee('Vann', '2.05.1998'),
                       salary.calculate_net_salary(590)])

for employee, salary in salary.employee:
    print(employee, salary)
