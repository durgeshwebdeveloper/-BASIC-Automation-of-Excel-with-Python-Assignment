    ### CSV BASICS
# => The CSV module 
# => File operation (open,close,write,read,append)
# =>with keyword for file handling
# =>csv.reader,csv.write, and writerows() functions
#  
#1. What is a CSV file?
# =>What is a CSV file and what is it's ues?
# A CSV (Comma Separated Values) file is a plain text file that stores tabular data where each line is a row and columns are separated by commas,
#  it is commonly used for storiing data like spreadsheets or databases.

#2.Introduction to the CSV module
# What is the CSV module in Python?
# The CSV module in Python is a built-in library used to handle CSV file operations like reading  and  writing tabular data.

#3.Create CSV file using the CSV module
# Write a Python program to create a CSV file named data.csv and store 3 records.
import csv
with open("data.csv","w", newline='') as f:
    write = csv.writer(f)
    write.writerow(["Name","Age"])
    write.writerow(["Durgesh",24])
    write.writerow(["Pratima",20])
    write.writerow(["Sanju",30])

#4. Open and close a file manually
#Show how to open and close a file manually.
f = open("file.txt","w")
f.write("Hello World")
f.close()

#5.Append data to file.
#Append "New line added" to a text file.
with open("file.txt","a") as f:
    f.write("\nNew line added")

#6.Read data from a text file
#Read all content from a file named file.txt.
with open("file.txt","r") as f:
    print(f.read())

#7.Write using the keyword
#Write a string to a file using with.
with open("sample.txt","w") as f:
    f.write("Python File Handling")

#8.Read CSV file using csv.reader()
#Read and print all rows from a CSV file.
with open("data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#9. Write CSV file csv.writer()
#Write names and scores to a CSV file.
import csv
with open("scores.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Score"])
    writer.writerow(["Durgesh",90])
    writer.writerow(["Sanju",100])

#10. Write multiple rows using writerows()
#Use writerows() to write data.
import csv 
data = [
    ["Name","City"],
    ["Durgesh","Delhi"],
    ["Sanju","Bengaluru"]
]
with open ("people.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#11. Skip header row while reading CSV.
# Read CSV excluding the header.
import csv 
with open("people.csv","r") as f:
    reader = csv.reader(f)
    next(reader)     #Skip header
    for row in reader:
        print(row)

#12. Count rows in CSV file
#Count how many rows are in data.csv
with open("data.csv","r") as f:
    reader = csv.reader(f)
    count = sum(1 for row in reader)
    print("Total rows: ",count)

#13.Store student info in CSV and read it.
#Save and retrieve student data from CSV.
import csv
#Writing
with open("students.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade"])
    writer.writerow(["Durgesh","A"])
    writer.writerow(["Sanju","A+"])

#Reading   
with open("students.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#14. Save Directory data into CSV file
import csv
data = [
    {"Name":"Durgesh","Age":21},
    {"Name": "Sanju","Age":30}
]
with open("dict_data.csv","w" ,newline='') as f:
    writer = csv.DictWriter(f,fieldnames=["Name","Age"])
    writer.writeheader()
    writer.writerows(data)

#15.Search for a name in a CSV file
import csv
name_to_search = "Durgesh"
with open("data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        if name_to_search in row:
            print("Found: ",row)

#16.Read CSV file and display only names
import csv 
with open("people.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print("Name: ", row[0])

#17. Count how many people are above 25 in a CSV.
import csv
count = 0
with open("data.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[1])>25:
            count += 1
print("People above 25: ",count)

#18.Create a marks.csv with 5 student marks.
import csv
marks = [
    ["Name","Marks"],
    ["Durgesh",49],
    ["Pratima",68],
    ["Sanju",100],
    ["Brahma",99.90],
    ["Anoop",99]
]
with open("marks.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(marks)

#19.Update a specific row in a CSV file (in-memory edit)
import csv
rows = []
with open("marks.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "Durgesh":
            row[1] == "100"
            rows.append(row)
with open("marks.csv","w",newline='')as f:
    writer = csv.writer(f)
    writer.writerows(rows)

#20. Create a csv attendance system.
import csv
with open("attendance.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Roll No.","Name", "Status"])
    for i in range(1,6):
        name = input("Enter name for Roll No.{i}:")
        status = input("Present/Absent.")
        writer.writerow([i,name,status])