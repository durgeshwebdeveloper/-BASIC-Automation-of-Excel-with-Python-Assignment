
#1.Create a Class and Object
#Write a class Car with attributes brand and year, and create an object:
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
c1 = Car("Toyota",2022)
print(c1.brand,c1.year)

#2.Add instance attributes using constructor
# Add color and mileage as attributes in a class:
class Vehicle:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
v = Vehicle("Red",12000)
print(v.color,v.mileage)

#3.Demonstrate Encapsulation
# Make a variable private using encapsulation 
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance   #private variable
    def show_balance(self):
        print("Banana: ",self.__balance)
acc = BankAccount(1000)
acc.show_balance()

#4.Use getter and setter methods 
class Student:
    def __init__(self):
        self.__name = ""
    def set__name(self,name):
        self.__name = name
    def get__name(self):
            return self.__name
s = Student()
s.set__name("Durgesh")
print(s.get__name())

#5.Single Inheritance Example
class Animal:
    def speak(self):
        print("Animal Speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.speak()
d.bark()

#6.Multiple Inheritance 
class  A:
    def showA(self):
        print("Class A")
class B:
    def showB(self):
        print("Class B")
        
class C(A,B):
    pass
obj = C()
obj.showA()
obj.showB()

#7.Multilevel Inheritance
class A:
    def methodA(self):
        print("A method")
class B(A):
    def  methodB(self):
        print("B method")
class C(B):
    def methodC(self):
        print("C method")
obj = C()
obj.methodA()
obj.methodB()
obj.methodC()

#8.Method Overriding
class Parent:
    def show(self):
        print("Parent Method")
class Child(Parent):
    def show(self):
        print("Child Method")
obj = Child()
obj.show()

#9.Use of super() in inheritance
class A():
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
obj = B()

#10. Constructor Overloading (via default arguments)
class Book:
    def __init__(self,title = None):
        if title:
            print("Book Title:",title)
        else:
            print("No title given")
b1 = Book()
b2 = Book("Python Guide")

#11. Method Overloading (via Default args)
class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c 
calc = Calculator()
print(calc.add(5))
print(calc.add(5,10))
print(calc.add(5,10,15))
