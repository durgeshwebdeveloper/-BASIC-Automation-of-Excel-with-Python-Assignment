#1.Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#2. Print even numbers between 1 and 20.
for i in range (2,21,2):
    print(i)

#3. Demonstrate the use of range (start,stop, step) with step=3 from 0 to 15.
for i in range(0, 16,3):
    print(i)

#4. While v/s For Loop
# Print numbers 1 to 5 using both while and for loops.
#(i). Using while loop
i = 1
while  i <= 5:
    print(i)
    i += 1

#(ii).Using for loop 
for i in range (1,6):
    print(i)

#5.For-Else Statement 
# Check if a number is prime using for-else
num = 13 
for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
    else:
        print("Prime")
    
#6.Nested For Loop
#Print a multiplication table (1 to 5).
for i in range(1,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()

#7.Factorial using for loop.
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
    print("Factorial: ", fact)

#8. Check if a number is a palindrome.
num = 121
rev = 0
temp = num
for digit in str(num):
    rev = int(str(num)[::-1])
print("Palindrome" if num == rev else " Not Palindrome")

#9. Check Armstrong number (3-digit).
num = 153
sum = 0
for digit in str(num):
    sum += int(digit)**3
    print("Armstrong " if sum == num else "Not Armstrong")

#10. List odd, even, and prime numbers from 1 to 20.
for i in range(1,21):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i,"Odd")

#11. Prime Check
for j in range(2,i):
    if i%j == 0:
        break
else:
    if i >1:
     print(i, "Prime")

#12. String Palindrome check using for loop.
s = "madam"
is_palindrome = True 
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        is_palindrome = False
        break
    print("Palindrome" if is_palindrome else "Not Palindrome")

#13. Print multiplication table of a given number.
n = 7
for i in range (1,11):
    print(f"{n} * {i} = {n * i}")

#14.Print right-angles triangle star pattern.
for i in range (1,6):
    print(" * " * i)

#15. Print inverted triangle pattern.
for i in range (5,0,-1):
    print(" * " * i)

#16. Fibonacci series using for loop (first 10 terms).
a, b = 0,1
for i in range(10):
    print(a,end = " ")
    a,b = b ,a+b

#17.Sum of digits using for loop.
num = 1234
sum_digits = 0
for d in str(num):
    sum_digits += int(d)
print("Sum of digits: ", sum_digits)

#18. Count vowels in a string.
s  = "Hello World"
count = 0
for char in s.lower():
    if char in  "aeiou":
        count +=1
print("Vowels: ",count)

#19. Find the largest number in a list.
nums = [ 10,25,7,98,34]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest: ",largest)

# #20.Check if a number is perfect (e.g.,28).
n = 28
sum = 0
for i in range  (1,n):
    if n % i == 0:
      sum += i
    print("Perfect Number" if sum == n else "Not Perfect")

#21.Generate a pyramid pattern
n = 5
for i in range(1,n+1):
    print(' '*(n-i) +'*' * (2*i - 1))