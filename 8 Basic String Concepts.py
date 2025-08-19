#1.What is a string? Create one and print it.
s = "Hello, Python!"
print(s)


#2. Use str() to convert a number into a string.
num = "100"
str_num = str(num)
print(str_num,type(str_num))

#3. Access the first and last character of a string.
s = "Python"
print("First:", s[0])
print("Last:", s[-1])

#4.Concatenate two strings.
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#5.Repeat a string 3 times.
s = "Hi"
print(s*3)

#String Slicing
#6.Slice "Python" from index 1 to 4
s = "Pyhton"
print(s[1:5])

#7.Reverse a string using slicing.
s = "Python"
print(s[::-1]) 

# String Length & Methods
#8.Use len() to find the length of a string.
s  = "Programming"
print(len(s))

#Convert a string to Uppercase.
s = "Pyhton"
print(s.upper())

#9.Capitalize only the first character of a string.
s = "hello world"
print(s.capitalize())

#Convert to title case.
s = "hello python world"
print(s.title())

#10.Swap the case of all letters.
s = "Hello PYTHON"
print(s.swapcase())

#String Type Checking Methods.
#11. Check if a string is alohabetic using isalpha().
s = "Hello"
print(s.isalpha())

#12. Check if a stirng is alphanumeric using isalnum().
s = "abc123"
print(s.isalnum())

#13.Check if a string is numeric using isdigit() and isnumeric().
s = "123"
print(s.isdigit(),)
#or
print(s.isnumeric())

#14.Use isascii() to check ASCII characters.
s = "Hello123"
print(s.isascii())

#15. Check if a string is a valid identifier. 
s = "var_name"
print(s.isidentifier())

#CONVERSION AND TRIMMING
#16.Convert a sentence into a list using split().
sentence = "Python is fun"
print(sentence.split())

#17. Remove spaces from both sides of a string.
s = "    Hello   "
print(s.strip())   #both sides
print(s.lstrip())   #left only
print(s.rstrip())   #right only

### Search and Replce 
#18. Use find() and replace() in a string.
s = "Python programming is fun"
print(s.find("programming"))
print(s.replace("fun","awesome"))
