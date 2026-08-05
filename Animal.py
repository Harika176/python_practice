class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("cat meows")
class Cow(Animal):
    def sound(self):
        print("cow moos")
d=Dog()
c=Cat()
w=Cow()
d.sound()
c.sound()
w.sound()