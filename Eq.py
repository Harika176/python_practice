class Student:
    def __init__(self,name):
        self.name=name
    def __eq__(self, other):
        return self.name == other.name
s1=Student("Rahul")
s2=Student("Rahul")
s3=Student("Riya")
print(s1==s2)
print(s1==s3)