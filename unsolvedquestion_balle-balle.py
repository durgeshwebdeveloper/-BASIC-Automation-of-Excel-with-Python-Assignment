#      Loops(For,While)
# 21.Print numbers from 1 to 10 using a loop.
# i = 1
# while i <= 10:
#   print(i)
#   i += 1

# # 22.Print the table of a  number uisng a loop.
# n  = 23
# i = 1
# while   i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i += 1

# 23.Find the factorial of a number using the while loop.
# num = 5
# fact = 1
# while num > 0:
#   fact *= num
#   num -= 1
#   print("Factorial: ",fact)

# 24.Print the reverse of a number.
#desi juggad =>% se lo , // se hatao, rev = rev*10 + digit lagao!
num = 7689
rev = 0
while num > 0:
    digit = num % 10  #last digit nikalo
    rev = rev * 10 + digit  #reverse number mein add kro
    num = num // 10  #number ko chhhota kro ( last digit hatao)
print("Reversed number is: ", rev)
# working : rev = 0
# 1234 %  10 = 4=> rev 0* 10 +4 = 4
# 123 -> 123%10 = 3 rev => 4 *10 +3 = 43
#12 -> 12 % 10 = 2 => rev = 443%10 + 2 = 432
# 1 -> 1 % 10 =  1 =>  rev = 432*10 +1 = 4321
 
# 25.Count the number of digits in a number.

# 26.Find the sum of all digits of a number.
# 27.Check whether a number is a palindrome.
# num = 121
# temp = num 
# rev = 0
# while num > 0:
#     rev = rev*10 + num %10
#     num //= 10
# if rev == temp:
#     print("Palindrome")
# 28.Check whether a number is an Armstrong number.
# 29. Generate  Fibonacci series up to n terms.
# 30. Print all numbers between 1 and 100.
# i = 1
# while i < 101:
#   print(i)
#   i += 1
