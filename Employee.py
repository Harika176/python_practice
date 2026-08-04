class Employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
class Manager(Employee):
    def __init__(self,name,employee_id,team_size):
        super().__init__(name,employee_id)
        self.team_size=team_size
    def display_info(self):
        print("Name:",self.name)
        print("Employee_id:",self.employee_id)
        print("Team_size:",self.team_size)
class Developer(Employee):
    def __init__(self, name, employee_id,programming_language):
        super().__init__(name, employee_id)
        self.programming_language=programming_language
    def display_info(self):
        print("Name:",self.name)
        print("Employee_id:",self.employee_id)
        print("Programming_language:",self.programming_language)
manager=Manager("Priyanka",101,7)
developer=Developer("Suchi",112,"Java")
manager.display_info()
developer.display_info()