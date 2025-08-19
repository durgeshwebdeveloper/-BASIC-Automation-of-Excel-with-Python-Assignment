# =>Chained Exceptions
# =>Nested try-except
# =>Custom Exception
# =>Re-raising Exception
# =>Logging Exception
# =>Exception handling in loops,functions,and file operations.
# =>Handling unexpected errors using Exception
# =>else and finally usage
# =>try-except-else-finally together

#1.Catch all unexpected exceptions
#=>Write a program that catches any unexpected exception.
try:
    a = int(input("Enter a number: "))
    b = 10 / a
except Exception as e:
    print("Unexpected error: ",e)

#2.Use try-except-else-finally together
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid Input")
else:
    print("Square is ",num**2)
finally:print("Operation complete")

#3.Nested try-except blocks
try:
    num = int(input("Enter number:"))
    try:
        result = 10/num
        print(result)
    except ZeroDivisionError:
     print("Division by Zero.")
except ValueError:
    print("Invalid Number.")

#4.Custom exeption class with attributes.
class CustomError(Exception):
   def _init_(self,message,code):
      super()._init_(message)
      self.code = code
      try:
         raise CustomError("Something went wrong",404)
      except CustomError as e:
         print((f"{e} - Code: {e.code}"))

#5.Re-raising exceptions
def check(num):
    try:
        if num<0:
            raise ValueError("Negative not allowed")
    except ValueError as e:
        print("Caught",e)
        raise      #Re-raise
try:
    check(-1)
except ValueError:
    print("Handled outside function.")

#6.Raise exception in loop
for i in range(3):
    try:
        num = int(input("Enter positive number:"))
        if num<0:
            raise ValueError("Only positive allowed")
    except ValueError as e:
        print("Error: ",e)

#7.Logging exceptions using logging module.
import logging
logging.basicConfig(filename="app.log",level=logging.ERROR)
try:
    1/0
except ZeroDivisionError as e:
    logging.error("Exception occured",exc_info= True)

#8.Using assert for advanced checks
def withdraw(balance,amount):
    assert amount <= balance, "Insufficient balance"
    return balance - amount
print(withdraw(100,50))   #OK
print(withdraw(100,200))   #Raises AssertionError

#9.Catching specific v/s general exceptions
try:
    x = int("abc")
except ValueError:
    print("Value Error")
except Exception:
    print("Some other error")

#10.File handling with specific error messages 
try:
    with open("file.txt","r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("File can't be read.")

#11.Catching TypeError in function
def add(a,b):
    return a+b
try:
    print(add(5,"hello"))
except TypeError:
    print("Cannot add int and str")

#12.Raising custom exceptions in a function 
class InvalidAge(Exception):
    pass
def check_age(age):
    if age<18:
        raise InvalidAge("Age must be 18+")
    return "Access Granted"
try:
    print(check_age(15))
except InvalidAge as e:
    print("Error:",e)

#13. Exception in List Access
try:
    lst = [1,2,3]
    print(lst[10])
except IndexError:
    print("Invalid index access.")

#14.Looping until correct input
while True:
    try:
        n =int(input("Enter a number:"))
        break
    except ValueError:
        print("Try again.")

#15.Clean-up action in finally
try:
    f = open("sample.txt","w")
    f.write("Hello")
except:
    print("Error Occured")
finally:
    f.close()
    print("File closed.")

#16.Catch KeyError in dictionary
data = {"name": "Alice"}
try:
    print(data["age"])
except KeyError:
    print("Key not found in dictionary.")

#17.Function that handles and logs errors
import logging
logging.basicConfig(level=logging.ERROR)
def divide(a,b):
    try:
        return a/b
    except Exception as e:
        logging.error("Error in divide()",exc_info=True)
    divide(5,0)

#18.Using pass in exception block
try:
    x = ("notanumber")
except ValueError:
    pass   #Do nothing
print("Program continues...")

#19.Handle multiple file errors 
try:
    with open("data,txt","r") as f:
        print(f.read())
except(FileNotFoundError,IOError) as e:
    print("File operation failed: ",e)

#20.Exception handling in class method
class Calculator:
    def divide(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "Cannot divide by zero."
calc = Calculator()
print(calc.divide(10,0))            