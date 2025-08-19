#1.Print numbers from 1 to 10
i = 1 
while i <= 10:
    print(i)
    i += 1

#2. Print even numbers from 2 to 20
i = 2 
while i <= 20:
    print(i)
    i += 2

#3. Sum of first 10 natural numbers.
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum: ", total)

#4. Factorial using while loop
num = 5
fact = 1
while num >0:
    fact *= num
    num -=1
print("Factorial: ", fact)

#5. Check if a number is palindrome (Integer)
num = 121
temp = num 
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")

#6. Armstrong number check.
num = 153
temp = num
result =  0
while temp > 0:
    digit = temp%10
    result += digit ** 3
    temp //= 10
if result == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

#7. Print all odd numbers from 1 to 50
i = 1 
while i <= 50:
    print(i,end = " ")
    i += 2

#8.Check if a number is prime.
num = 29
i =2
is_prime = True
while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1
print("Prime " if is_prime else "Not Prime")

#9. print multiplication table of a number
num = 5
i = 1
while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i += 1
    
 #10. Print digits of a number in reverse.
num = 12345
while num > 0:
    digit = num % 10
    print(digit, end = " ")
    num //=  10 

#11 Count numbers of digits
num = 123456
count = 0
while num > 0 :
    count += 1
    num //= 10
    print("Total digits: ",count)

#12.Sum of digits
num = 1234
total = 0 
while num > 0 :
    total += num % 10
    num //= 10
    print("Sum of digits: ", total)

#13. Reverse a string  using while loop
# s = "python"
# i = len(s) - 1 
# rev = 0
# while i >= 0:
#     rev += s[i]
#     i -= 1
#     print("Reversed: ", rev)

#14.String palindrome using while loop
s = "madam"
i = 0 
j = len(s) - 1
is_palinddrome = True
while i < j:
    if s[i] != s[j]:
        is_palinddrome = False
        break
    i += 1
    j -= 1
    print("Palindrome" if is_palinddrome else "Not Palindrome")

#15.use of While-else
n = 5
while n > 0:
    print(n)
    n -= 1
else:
    print("Loop Completed")

#16. Nested while: Print pattern 
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

#17.Find the smallest divisor of a number (other than 1)
num = 91
i = 2
while i <= num:
    if num % i == 0:
        print("Smallest divisor: ", i)
        break
    i += 1

#18. Print first 10 Fibonacci numbers
a, b = 0,1
count = 0
while count < 10:
    print(a , end = " ")
    a,b = b, a+b
    count += 1

#19. Find GCD of two numbers using subtraction
a, b = 48,18 
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print("GCD: ",a)

#20.keep taking input until user types 'exit'
while True:
    cmd = input("Enter command (type 'exit' to quit): ")
    if cmd == "exit":
        print("Goodbye!")
        break
    print("You entered: ",cmd)