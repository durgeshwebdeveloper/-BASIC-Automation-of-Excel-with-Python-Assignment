#1.Declare variables of different data types and print them.
a = 10   #Integer
b = 3.14   #Float
c = "Python"   #String
d = True    #Boolean
print(a,b,c,d)

#2. Check if a list is mutable.
lst = [1,2,3]
lst[0] = 10
print(lst)   #Lists are mutable

#3. Check if a tuple is immutable.
tpl = (1,2,3)
# tpl[0] = 10  #This will raise an error
print("Tuples are immutable")

#4. Show the use of arithmetic operators.
a = 20
b = 3
print(a+b, a-b, a*b, a/b, a%b, a//b, a**b)

#5.Demonstrate comparison operators.
x = 5
y = 7
print(x == y, x>7, x<y,x>=y, x<=y)

#6. Use logical operators.
a = True
b = False
print( a and b)   #False
print( a or b)    #True
print(not a)  #False

#7.Show assignment operator chaining.
x = y = z = 10
print(x,y,z)

#8.Demonstrate membership operators.
fruits = ["apple","banana","cherry"]
print("apple" in fruits)
print("grape" not in fruits )

#9. Show identity operator usage.
a = [ 1,2,3]
b = a 
c = [1,2,3]
print(a is b)   #True
print(a is c)   #False
print(a == c)   #True

#10. Demonstrate bitwise operator.
a = 5   #0101
b = 3   #0011
print(a & b)   #AND = 0001 = 1
print( a|b)   #OR = 0111 = 7
print(a ^ b)   #XOR = 0110 = 6

#11.Use left and right shift operator.
a = 8   #1000
print(a << 1)    #16(Left shift)
print(a >> 2)    #2(Right shift)

#12. Demonstrate Boolean operators in conditions.
x = 10
y = 20
if x<y and y>15:
    print("Both conditions are True")

#13.Perform implicit typr casting.
a = 5
b = 2.0
result = a+b     #int+float = float
print(result,type(result))

#14. Perform explicit type casting.
a = 10
b = float(a)
print(b,type(b))    #10.0   <class  'float'>

#15. Use ord() and chr() functions.
print(ord("A"))    #65
print(chr(66))    #B

#16.Determine variable types using type().
a = "Python"
b = 10
print(type(a), type(b))

#17.Swap two variables without using third variable.
a = 5
b = 10
a,b = b,a
print("a:",a,"b:",b)

#18. Write a program to check if a number is even using % operator.
num = 6
if num%2 == 0:
    print("Even")
else:
    print("Odd")    

#19.Concatenate strings using + operato.
first = "Hello"
last = "World"
print(first + " "+last)

#20. Add a number and a string using type casting.
num = 10 
text = "5"
result = num + int(text)
print(result)