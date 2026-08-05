class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Subject:",self.subject)
student=Student("Suchi",20,90)
teacher=Teacher("Madhavi",40,"Science")
student.display_info()
teacher.display_info()