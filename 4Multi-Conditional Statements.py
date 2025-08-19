#1. Write a program that takes a percentage and prints the grade based on:
#-> 90+ = A
#-> 80-89 = B
#-> 70-79 = C
#-> 60-60 = D
#-> Below 60 = F
percent = float(input("Enter percentage: "))
if percent >= 90:
    print("Grade A")
elif percent >=80:
    print("GRade B")
elif percent >= 70:
    print("Grade C")
elif percent >= 60:
    print("Grade D")
else: 
    print("Grade F")

#2. Traffic light Simulation.
#Ask for a color and ssimulate a traffic light:
#->red-->"Stop"
#->yellow-->"Ready"
#->green-->"Go"
color = input("Enter traffic light color: ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid Color")

#3. Day of the week with elif
# Input a number (1 t0 7) and print the corresponding day of the week.
num = int(input("Enter a number (1-7)"))
if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("Invalid Number")

#4. Movie ticket price based on age
#Use elif to set ticket prices:
#->Below 5: Free
#->5-12: 5$
#->13-60: 10$
#->Above 60 : 7$
age = int(input("Enter your age: "))
if age < 5 :
    print("Free Ticket")
elif age <=12:
    print("Ticket Price : $5")
elif age <= 60:
    print("Ticket Price: $10")
else:
    print("Ticket Price : $7")

#5. Menu-based calculator using elif
# Ask for  two numbers and a choice of operation: add, subtract, multiply,divide.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (add/sub/mul/div): ").lower()
if op == "add":
    print("Result: ", a+b)
elif op == "sub":
    print("Result: ",a-b)
elif op == "mul":
    print("Result:",a*b)
elif op == "div":
    print("Result:",a/b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid operation")

#6. Income tax slab checker.
# Print tax slab based on income:
# -> <=2.5L : No tax
# -> 2.5-5L : 5%
# -> 5-10L : 20%
# -> 10L : 30%
income = float(input("Enter annual income(in Lacs)"))
if income <=2.5:
    print("No Tax")
elif income <= 5:
    print("5% Tax")
elif income <= 10:
    print("20% Tax")
else:
    print("30% Tax")

#7. Find the largest of three numbers using nested if-else:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third: "))
if a>b:
    if a>c:
        print("Largest is a:  ", a)
    else:
        print("Largesht is c: ",c)
else:
    if b >c:
        print("Largest is b: ",b)
    else:
        print("Largest is c: ",c)

#8.Determine category of a number.
# Input a number and categorize:
#->Negative
#->Zero
#->Small (1-10)
#->Medium (11-100)
#->Large (above 100)
num = float(input("Enter Number: "))
if num<0:
    print("Negative Number")
elif num == 0:
    print("Zero")
elif num <= 10:
    print("Small Number")
elif num <=100:
    print("Medium Number")
else:
    print("Large Number")

#9. Exam result checker (nested elif)
# If marks are above 90, say "Excellent", between 75-90 --> "Good", 60-74 -->"Average", below 60 -->"Fail"
marks = int(input("Enter marks: "))
if marks >90:
    print("Excellent")
elif marks >=75:
    print("Good")
elif marks >=60:
    print("Average")
else:
    print("Fail")

#10. Month name using elif
# Take a number (1-12) and print month name.
month = int(input("Enter month number(1-12): "))
if month == 1:
    print("January")
elif month == 2 :
    print("February")
elif month == 3 :
    print("March")
elif month == 4 :
    print("April")
elif month == 5 :
    print("May")
elif month == 6 :
    print("June")
elif month == 7 :
    print("July")                
elif month == 8 :
    print("August")
elif month == 9 :
    print("September")
elif month == 10 :
    print("October")
elif month == 11 :
    print("November")
elif month == 12 :
    print("December")

#11.Categorize temperature (nested elif)
# Input temp and print:
#-> <0:"Freezing"
#-> 0-5: "Cold"
#-> 26-35: "Warm"
#-> 35: "Hot"
temp = float(input("Enter temperature: "))
if temp < 0 :
    print("Freezing")
elif temp <=15:
    print("Cold")
elif temp <=25:
    print("Pleasant")
elif temp <=35:
    print("Warm")
else:
    print("Hot")

#12. Check even/odd and positive/negative using nested if
num = int(input("Enter a number: "))
if num % 2 == 0:
    if num > 0:
        print("Positive Even")
    else :
        print("Negative Even")
else:
    if num > 0:
        print("Positive Odd")
    else :
        print("Negative Odd")

#13. Car Speed check
# Speed check:
#-> <40:"Too slow"
#->40-60: "Safe speed"
#->61-100: "Fast"
#->100: "Over - Speeding"
speed = int(input("Enter speed: "))
if speed <40:
    print("Too slow")
elif speed <=60:
    print("Safe  speed")
elif speed <=100:
    print("Fast")
else:
    print("Over-Speeding") 

#14. Student performance evaluator
# Input attendance% and marks. Eligilble only if attendance >= 75 and marks >=40.
attendance = float(input("Attendance % : "))
marks = float(input("Marks: "))
if attendance >= 75:
    if marks >= 40:
        print("Passed")
    else:
        print("Failed in marks")
else:
    print("Ineligible due to low attendance")

#15.Restaurant bill discount
#-> <500 --> no discount 
#-> 500-999 --> 5%
#-> 1000-1999 --> 10%
#-> >= 2000 --> 15%
bill = float(input("Enter total bill: "))
if bill >= 2000:
    discount = 0.15
elif bill >= 1000:
    discount = 0.10
elif bill >= 500:
    discount = 0.05
else:
    discount  = 0    
final = bill - (bill*discount)
print(f"Final amount:{final:2f}")

#16. Print even/odd/natural/zero
n = int(input("Enter number:"))
if n == 0:
    print("Zero")
elif n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative Number")        

#17. Alphabet type check
# Check if a letter is:
# -> vowel
# ->Consonant
# ->Not a letter
ch = input("Enter a character: ")
if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")

#18.BMI Calculator
bmi = float(input("Enter your BMI"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal Weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
 
#19. Nested Elif: SmartPhone price range
price = int(input("Enter phone price: "))
if price < 10000:
    print("Budget Phone")
elif price <20000:
    print("Mid-Range Phone")
elif price < 50000:
    print("High-end  Phone")
else:
    print("Premium Phone")

#20. Nested if for library fine
# If a book is returned late:
#-> <=5days --> Rs.5/day
#-> 6-10days -->Rs.10/day
# 10 days --> Rs.16/day +Rs. 100 penalty
days = int(input("Days late."))
if days >0:
    if days <=5:
        fine = days * 5
    elif days <= 10:
        fine = days * 10
    else:
        fine = days * 15 + 100
        print("Total fine: ",fine)
else:
 print("No fine")