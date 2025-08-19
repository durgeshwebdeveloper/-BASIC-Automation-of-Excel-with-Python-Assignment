#1. Print "Hello, World! in Python."
print("Hello World!")

#2.Write a  Python program to print your name and age.
name = "Durgesh"
age = 18
print("Name: ",name)
print("Age: ",age) 

#3.Write a program to show Python version using a built-in module.
import sys 
print("Python version: ",sys.version)

#4.Create a multi-line string describing the history of Python.
history = '''
Python was created by Guido van Rossium in 1991.
It was designed to be simple and easy to read.
Its names comes from Monty Python's Flying Circus.'''
print(history)

#5.Print the current working directory using Python.
import os 
print("Current Direcotry: ", os.getcwd())

#6. Use a function to display a welcome message.
def welcome():
    print("Welcome to python programming! ")
welcome()

#7. Create a program that adds two numbers entered by the user.
a = int(input("Enter the first number: "))
b = int(input("Enter second number: "))
print("Sum is : ", a + b)

#8. Write a program to determine the data type of a variable.
x = 10 
print(type(x))

#9. Create a Python file that prints "Setup Successful!"
# Save as basic.py:
print("Setup Successfull!")

#10. Use  Python in VS Code to print the current date.
from datetime import date
print("Today's date is:",date.today())

#11. Use the ord() function to print Unicode of a character.
print(ord('A'))

#12. Use the chr() function to print character from Unicode.
print(chr(97))

#13. Run a Python file from terminal and print system info.
import platform
print("System:", platform.system())
print("Python Version:",platform.python_version())

#14. Write a program that prints all keywords in Python.
import keyword
print("Python Keywords:\n",keyword.kwlist)

#15. Accept input for name and greet the user.
name = input("Enter your name:")
print("Hello,",name)

#16.Write a program to swap two number.
a = 5
b =10
a,b = b,a
print("a:",a,"b:",b)

#17. Print the value of PI using the math module.
import math
print("Value of PI is: ",math.pi)

#18. Create a simple calculator using basic function.
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
print("Addition: ",add(4,3))
print("Subtraction: ;",sub(9,3))

#19. Write a program that checks if Python is installed.
import sys
print("Python Executable Path:",sys.executable)

#20.Write and run a Python program using VS Code that prints ASCII art.
print(r)