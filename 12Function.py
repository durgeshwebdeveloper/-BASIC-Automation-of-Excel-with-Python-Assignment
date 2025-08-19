
#1. What is a function in Python?
# A function is a reusable block of code.
def greet():
    print("Hello World!")
greet()

#2.Define a function that prints a welcome message.
def welcome():
    print("Welcome to Python programming!")
welcome()

#3. Define a function that adds two numbers.
def add(a,b):
    print("Sum: ",a+b)
add(5,3)

#4. Create a function that returns the square of a number.
def square(n):
    return n*n
print(square(4))

#5. Show the syntax of a function declaration.
#Syntax:
# def function_name(parameters):
#body of the function
def say_hi():
    print("Hi!")
say_hi()

#6.Function with default parameter value
def greet(name = "Guest"):
    print("Hello", name)
greet()
greet("Alice")

#7.Call a function with parameters.
def multiply(x,y):
    return x*y
print(multiply(8,9))

#8.Function with return statement.
def cube(n):
    return n**3
result = cube(3)
print(result)

#9. Function to check if a number is even or odd.
def check_even(n):
    if n %2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(8))

#10.Function to calculate factorial of a number.
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(factorial(5))

#11. Function to find the largest of two numbers.
def largest(a,b):
    return a if  a>b else b 
print(largest(23,45))

#12. Function that returns multiple values.
def operations(a,b):
    return a+b,a-b

add,sub = operations(10,5)
print("Sum: ", add, "Difference: ", sub)

# #13. Function to count vowels in a string.
# def count_vowels(text):
#     count = 0
#     for ch in text:
#         if ch.lower() in 'aeiou':
#             count += 1
#         return count
# print(count_vowels("durgesh"))

#14. Function to reverse a string.
def reverse_strings(s):
    return s[::-1]
print(reverse_strings("python"))

#15. Function to check if a string is a Palindrome.
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

#16. Function to calculate average of three numbers.
def average(a,b,c):
    return a+b+c/3
print(average(4,8,10))

#17. Function to check prime numbers.
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(13))

#18. Function that prints table of a number.
def print_table(n):
    for i in range(1,11):
        print(f"{n}*{i} = {n*i}")
print_table(5)

#19. Function with no arguments and no return 
def greet():
    print("Good Morning!")
greet()    

#20. Function that returns the length of a list
def list_length(lst):
    return len(lst)
print(list_length([1,2,3,4,5]))