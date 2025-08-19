#12. Polymorphism using functions
def add(a,b):
    return a+b
print(add(5,3))
print(add("Hello "," World"))

#13.Polymorphism using classes
class Cat:
    def speak(self):
        print("Meow")
class Dog:
    def speak(self):
        print("Bark")
for animal in (Cat(),Dog()):
     animal.speak()

#14. Abstract class with abc Module
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
        def area(self):
            return 3.14*5*5
c = Circle()
print(c.area())
         
#15.Data hiding and abstraction
class Employee:
    def __init__(self,salary):
          self.__salary = salary   #hidden
    def get_salary(self):
         return self.__salary
e = Employee(500000)
print(e.get_salary())

# 16. Interface-like behavior in Python
from abc import ABC , abstractmethod
class Animal(ABC):
     @abstractmethod
     def sound(self):
          pass
class Dog(Animal):
          def sound(self):
               print("Bark")
d = Dog()
d.sound()

#17.Class with class variable and  instance method
class Student:
     school = "ABC School"   #class variable
     def __init__(self,name):
          self.name = name
     def display(self):
          print(self.name,"-",Student.school)
s1 = Student("Durgesh")
s1.display()

#18.Class method v/s Static method
class Example:
     @classmethod
     def show_class(cls):
          print("Class Method")
     @staticmethod
     def show_static():
      print("Static Method")
Example.show_class()
Example.show_static()

#19.Demonstrate isinstance() with OOP
class Teacher:
     pass
t = Teacher()
print(isinstance(t,Teacher))

#20. Create a real-world example using inheritance and encapsulation 
class Person:
     def __init__(self,name,age):
          self.__name = name
          self.__age = age
     def get_info(self):
          return self.__name, self.__age
class Student(Person):
     def __init__(self,name,age,student_id):
          super().__init__(name,age)
          self.student_id= student_id
s= Student("Durgesh", 18, "S1001")
print(s.get_info())
print(s.student_id)
