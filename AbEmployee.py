from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        salary=30000
        print("Full Time Salary:",salary)
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        hours=20
        rate=500
        salary=hours*rate
        print("Part Time Salary:",salary)
e1=FullTimeEmployee()
e2=PartTimeEmployee()
e1.calculate_salary()
e2.calculate_salary()