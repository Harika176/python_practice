class Employee:
    def __init__(self,emp_name):
        self.emp_name=emp_name
    def __eq__(self,other_name):
        return self.emp_name==other_name.emp_name
e1=Employee("madhavi")
e2=Employee("suchithra")
e3=Employee("madhavi")
print(e1==e2)
print(e1==e3)