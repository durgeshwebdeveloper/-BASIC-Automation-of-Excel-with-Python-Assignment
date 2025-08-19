#1. How to print Output in Python?
# Write a pyhton program to print "Hello,World!"
 
#2. How to take input from the user using input()?
# Write a python program to take a user's name and print it.
name = input("Enter your name: ")
print("Hello", name)
 
#3.Difference between input() and raw_input() (Python 2 only)?
#Explain the difference between input() and raw_input() in Pyhton 2.
#-> raw_input() reads input as a string.
#-> input() evaluates the input as a Python expressions.
# In Python 3, only input() exists and behaves like raw_input().

#4.How to create a file in Python?
# Write a Python program to create a file named example.txt.
f = open("example.txt","w")
f.write("File created!")
f.close()

#5. How to read data from the keyboard and print it?
# Read an integer from the keyboard and print its square.
num = int(input("Enter a number:"))
print("Square is : ", num ** 2)  

#6. How to open and close a file?
#Open a file sample.txt for wirting, write text, and then close it.
f = open("sample.txt","w")
f.write("This is a test file.")
f.close()

#7.How to read a file line by line?
# Write a Python Program to read all lines from durgesh.txt.
with open("durgesh.txt","r") as f:
    for line in f:
        print(line.strip())

#8.How to write multiple lines to a file?
# Write 3 lines to a file lines.txt.
lines = ["First lines\n","Second line\n","Third line\n"]
with open ("lines.txt","w") as f:
    f.writelines(lines)

#9. How to append data to a file?
# Append "New entry" to log.txt.
with open("log.txt","a") as f:
    f.write("New entry\n")

#10. How to read the entire file content  at  once?
# Read and print full content of durgesh.txt.
with open("durgesh.txt","r") as f:
    content = f.read()
    print(content)

#11. Write a program to count words in a file.
with open("durgesh.txt","r") as f:
    content = f.read()
    words = content.split()
    print("Words count.",len(words))

#12.Write a program to copy content from one file to another .
with open("durgesh.txt","r") as src,open("sample.txt","w") as dest:
    dest.write(src.read())

#13. Check if a file exists before opening.
import os 
if os.path.exists("check.txt"):
    with open("check.txt") as f:
        print(f.read())    
else:
    print("File does not exist.")

#14.Write a program to count lines in a file.
with open("durgesh.txt","r") as f:
    lines = f.readlines()
    print("Total Lines: ", len(lines))
#15.How to use with statement for file handling?
with open("myfile.txt","w") as f:
    f.write("Using with statement.")
#Automatically Handles closing of file.

#16.Write a program to reverse the content of a file.
with open("myfile.txt","r") as f:
    data = f.read()
    with open("reversed.txt","w") as f:
        f.write(data[::-1])


#17. How to read specific number of characters from a file?
with open("myfile.txt","r") as f:
    print(f.read(10))    #reads first 10 characters

#18.Write a program to search for a word in a file.
word = "Python"
with open("sample.txt","r") as f:
    content = f.read()
    if word in content:
        print("Word found bhai!")
    else:
        print("Word not found bhai!")

#19. Write a program to remove blank lines  from a file.
with open("sample.txt","r") as f:
    lines = f.readlines()
    with open("output.txt","w") as f:
        for line in lines:
            if line.strip():
                f.write(line)

#20.File Handling Program : Store and display student names and marks.
#Writing to file
with open ("students.txt","w") as f:
    for i in range(3):
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        f.write(f"{name},{marks}\n")

#Reading file
with open("students.txt","r") as f:
    for line in f:
        name,marks = line.strip().split(',')
        print(f"Name:{name},Marks:{marks}") 
