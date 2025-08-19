#1.What is an Exception?
#What is an exception?
# => An exception is an error that occurs during the execution of a program and disripts its
# normal flow. Python provides mechanisms to handle these exceptions using try,except,finally,etc. 

#2. List common types of errors in Python.
#Name 5 common error types in Python.
# =>SyntaxError
# =>NameError
# =>ValueError
# =>ZeroDivisionError
# =>FileNotFoundError
# =>FileExistsError

#3. Difference between common error types.
#Match the error with its cause:
#     Error                     Cause
# SyntaxError         =>         Invalid Syntax
# NameError           =>         Using variable before declaring
# ValueError          =>         Invalid value for a function
# ZeroDivisionError   =>         Dividing by zero
# FileNotFoundError   =>         Trying to open a non-existent file
# IndentationError    =>         Incorrect Indentation

#4.How  are exceptions generated?
#Show a program that generates a ZeroDivisionError. 
a = 10
b = 0
print(a/b)  #Generates ZeroDivisionError

#5.Simple exception handling using try-except
#Handle a division by zero error.
try:
    x = 10/0
except ZeroDivisionError:
    print("You cannot divide by zero.")

#6.Catch multiple exceptions.
#Handle both ZeroDivisonError and ValueError.
try:
    num = int(input("Enter number:"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.Please enter a number.")

#7. Use of finally block
#Show a program that prints a message no matter what.
try:
    a = 5/0
except ZeroDivisionError:
    print("Handled division error.")
finally:
    print("This always executes.")

#8.Exception while opening a file
#Handle file not found error.
try:
    f = open("nofile.txt","r")
except FileNotFoundError:
    print("File does not exist.")

#9.Exception handling with file reading
#Read from a file and handle error if it doesn't exist.
try:
    with open("example.txt","r") as f:
        print(f.read())
except FileNotFoundError:
 print("File not found.")
    
#10.Raise a custom exception manualy
age = int(input("Enter age:"))
if age < 18:
   raise Exception("You must be atleast 18 years old.")    

#Using asset keyword.
#11.Assert that a number is positive.
x = -10
assert x>0, "x must be positive" 

#12.Create a custom exception class
class MyError(Exception):
    pass
raise MyError("This is a custom error")


#13.Handle custom exception
class AgeError(Exception):
    pass
try:
    age = int(input("Enter age:"))
    if age<18:
        raise AgeError("Underage not allowed")
except AgeError as e:
    print(e)     

#14.Use else with exception handling
try:
    num = int(input("Enter number:"))
except ValueError:
    print("Not a number.")
else:
    print("Square is: ",num**2)

#15.Handle list index error
try:
    lst = [1,2,3]
    print(lst[5])
except IndexError:
    print("Index out of range:") 

#16.Multiple exceptions in one block
try:
    a = int("abc")
except(ValueError,TypeError) as e:
    print("Error:",e)    

#17.Demonstrate finally closing file
try:
    f = open("test.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File missing.")
finally:
    print("Closing operation done.")

#18.Input validation using exception 
try:
    x = int(input("Enter a number:"))
    print("Double is ",x*2)
except ValueError:
    print("That's not a valid number.")

#19.Program with raise and finally
def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Can't divide by 0")
    return a/b
try:
    print(divide(10,0))
except ZeroDivisionError as e:
    print(e)
finally:
    print("Execution complete.")

#20.Custom exception: NegativeNumberError
class NegativeNumberError(Exception):
    pass
try:
    number = int(input("Enter positive number: "))
    if number <0:
        raise(NegativeNumberError("Negative Number not allowed"))
    print("Square is ", number** 2)
except NegativeNumberError as e:
    print("Custom Error",e)