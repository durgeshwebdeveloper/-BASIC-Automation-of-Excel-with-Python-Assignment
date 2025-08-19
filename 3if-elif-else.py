#1.Check if a number is positive using an if-statement.
#=>Write a program that reads a number and prints "Positive" if the number is greater than zero.
num = float(input("Enter a number: "))
if num > 0 :
    print("Positive")

#2. Use an if-else statement to check if a number is positive or neagtive.
#=>Write a program that prints "Positive" if the entered number is above 0; otherwise, print "Negative".
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")

#3.Identify if a number is positive,negative or zero using nested if-else.
# =>Extend the previous program to print "Zero" using nested if-else.
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
        print("Zero")
else:
     print("Negative")

#4. Determine passing status based on marks.
# =>Write a program where the user enters their mark.Print "Pass" if marks are greater tha or equal to 40, otherwise "Fail".
marks = float(input("Enter your marks:"))
if marks >=40:
     print("Pass")
else:
     print("Fail")

#5. Nested if-else for scholarship eligibility.
#=>Write a program for a student applying for a scholarship. If the students's marks are 85 or above, 
# then check if they belong to a reserved category.
#->If yes, print "Eligibile for Scholarship".
#->If not, print "Needs additonal critera".
#->If marks are below 85, print "Not Eligible".
marks = float(input("Enter your marks: "))
if marks >= 85:
     category = input("Are you from a reserved category? (yes/no): ").strip().lower()
     if category =="yes":
          print("Eligible for Scholarship")
     else:
          print("Needs additional criteria")
else:
     print("Not Eligible")          

#6.ATM withdrawal simulation.
#=> Simulate an ATM where a user can withdraw money.
#->Check if the account balance is sufficient for the withdrawal.
#->If the balance is enough and the requested amount is a multiple of 10, allow withdrawal : otherwise, print the respective error message.
balance = 500
withdrawal= int(input("Enter amount to withdraw:"))
if withdrawal % 10 ==0:
     if withdrawal<= balance:
          balance -= withdrawal
          print("Withdrawal Successful ! New balance", balance)
     else:
          print("Insufficient balance")
else:
     print("Amount must be in multiples of 10.")

#7. Check leap year.
# Write a program fo verify if a given year is a leap year.
# A year is a leap year if it is divisible by 4, but not by 100 unless it is also divisibleby 400.
year = int(input("Enter a year:"))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     print(year, "is a leap year")
else:
     print(year, "is not a leap year")

#8. Voting Eligibility Check.
# Write a program that takes the user's age prints "Eligibile to vote " if 18 or older,and "Not elilgible" otherwise.
age = int(input("Enter your age: "))
if age >= 18:
     print("Eligible to vote")
else:
     print("Not eligible")

#9. Greet a user based on age.
# Write a program that asks for the user's name and age. If the age is less than 18, print "Hello[Name], you are a minor", otherwise print "Hello[Name],welcome!".
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 18:
     print("Hello", name + ", you are a minor.")
else:
     print("Hello", name +",welcome!" )

#10. Check if a letter is a vowel or consonant.
# Write a program that reads a single character and prints "Vowel" if it is a vowel, otherwise "Consonant".
ch = input("Enter a letter: ").lower()
if ch in "aeiou":
     print("Vowel")
else:
     print("Consonant")

#11. Even or odd number check
# Write a program that determines if the input number is "Even" or "Odd".
num = int(input("Enter a number: "))
if num % 2 == 0:
     print("Even")
else:
     print("Odd")

#12. Check username validity.
# Write a program that checks if a username is valid. The criteria are: username must be atleast 5 characters long.
username = input("Enter username: ")
if len(username)>=5:
     print("Username accepted")
else:
     print("Username too short")

#13. Strong password checker.
#Write a program that checks if a password is strong. Assume a strong password must be atleast 8 characters long and contain both letters and number
#->Print "Strong password " if it meets criteria; otherwise, print "Weak Password".
password = input("Enter password: ")
if len(password)>=8 and any(ch.isdigit() for ch in password) and any (ch.isalpha() for ch in password):
     print("Strong Password")
else:
     print("Weak password")

#14. Find the largest of three numbers using nested if-else:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number:"))
if a >= b:
     if a >=c:
          largest = a
     else:
          largest = c
else:
     if b>=c:
          largest = b 
     else:
          largest = c
print("The largest number is ", largest)

#15. Simple Calculator with operator selection.
# Write a program where  user enters two numbers and selects an operations(+ or -)
# Perform the operation using if-elif statements.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number"))
operator = input("Enter Operator(+ or -): ")
if operator == "+":
     print("Result: ", num1 + num1)
elif operator == "-":
     print("Result:  ", num1 - num2)
else:
     print("Invalid operatof")       

#16. Categorize age groups.
# Write a program that categories a person by age.
#-> if age <13: "Child"
#-> if age is between 13 and 19 (inclusive): "Teenager"
#->if age is between 20 and 64:"Adult"
#-> Otherwise "Senior"
age = int(input("Enter  your age: "))
if age<13:
     print("Child")
elif 13<=age<=19:
     print("Teenager")
elif 20<=age<=64:
     print("Adult")
else:
     print("Senior")

#17. Grade categorization using nested if-else.
# Write a program that assigns a letter grade based on a numerical score:
#-> 90 and above: "A"
#-> 80-89: "B"
#-> 70-79: "C"
#-> 60-69: "D"
#-> Below 60: "F"
score = float(input("Enter the score: "))
if score >=90:
     grade = "A"
else:
     if score >= 80:
          grade = "B"
     else:
          if score >= 70:
               grade = " C "
          else:
               if score >= 60:
                    grade = "D"
               else:grade = "F"
               print("Grade", grade)

#18. Provide weather advice based on temperature.
# Write a program that reads the temperature (in C degree) and prints.
# -> "It's hot!" above 30,
# -> "It's warm." if between 20 and 30,
# -> "It's chilly." if between 10 and 19,
# ->"It's cold!" Otherwise.
temp = float(input("Enter the temperature in C degree: "))
if temp > 30:
     print("It's hot!")
elif temp >= 20:
     print("It's warm.")
elif temp >= 10:
     print("It's chilly.")
else:
     print("It's cold!") 
       
#19. Determine if a day is a weekend or weekday.
#Write a program that asks the user to enter a day of the week and prints " Weekend" if the day is Saturday or Sunday, otherwise "Weekday".
day = input("Enter the day of the week: ").strip().lower()
if day == "saturday" or day == "sunday":
     print("Weekend")
else:
     print("Weekday")
     
#20. Check driving license eligibility using nested conditions.
# Write a program that checks if a user is eligible for a driving license.The user must be
# atleast 18 years old and have pased a vision test (answer "pass"). If both conditions are met, print "Eligible for diving license", otherwise print 
# the appropriate reason.
age = int(input("Enter your age: "))
vision = input("Did you pass the vision test? (pass/fail): ").strip().lower()
if age >= 18:
     if vision == "pass":
          print("Eligible for driving license")
     else:
          print("Not eligible due to vision test failure")
else:
     print("Not eligible due to age restriction")     