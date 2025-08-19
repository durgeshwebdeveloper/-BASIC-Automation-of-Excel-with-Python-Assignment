    ####   List Basics and Access   ###
#1.Create a list of 5  integers and print it.
numbers = [10,20,30,40,50]
print(numbers)

#2. Why is a list called a mutable data type? Show an example.
fruits = ["apple","banana","cherry"]
fruits[1] = "orange"
print(fruits)   #banana is replaced ,showing mutablility

#3.Represent a list with mixed data types.
info = ["Alice",25,5,6,True]
print(info)

#4.Difference between string and list with an example.
s = "hello"
l = ['h','e','l','l','o']
print(s[1])    #e
print(l[1])    #e
## STRING IS IMMUTABLE,LIST IS MUTABLE.

#5. Access the 2nd and last element in list.
data = [5,10,15,20,25]
print(data[1])   #10
print(data[-1])   #25

#Slicing and Iteration
#6. Slice and print first 3 elements of a list.
nums = [1,2,3,4,5]
print(nums[:3])

#7. Use a for loop to print each element of a list
colors = ["red","green","blue"]
for color in colors:
    print(color)

##LIST FUNCTIONS AND METHODS
#8. Use len() to find length of a list.
items = [1,2,3,4]
print(len(items))

#9. Add an element to the end using append().
names = ["John", "Doe"]
names.append("Smith")
print(names)

#10. Insert an element at index 1 using insert().
marks = [50,60,70]
marks.insert(1,55)
print(marks)

#11.Extend a list with another list.
a = [1,2]
b = [3,4]
a.extend(b)
print(b)

#12. Use pop() to remove the last element.
fruits = ["apple","banana","cherry"]
fruits.pop()
print(fruits)

#13. Use remove() to delete a specific value.
items = [1,2,3,2]
items.remove(2)
print(items)  #removes first occurence of 2.

#14.Use del to delete item at index 1.
data = [100,200,300]
del data[1]
print(data)

#Aggregations and Analysis
#15. Find the sum,max and min of a list.
values = [10,20,30]
print("Sum: ",sum(values))
print("Max: ",max(values))
print("Min: ",min(values))

#16. Use count() to count occurrences of 2.
numbers = [1,2,2,3,2,4]
print(numbers.count(2))

#17.Sort a list in ascending order.
nums  = [4,1,3,2]
nums.sort()
print(nums)

#18.Reverse a list using reverse()
nums   = [1,2,3]
nums.reverse()
print(nums)

##COPY AND CLEAR
#19.Copy a list using copy()method.
a = [1,2,3]
b = a.copy()
print(b)

#20.Clear all elements using clear().
items = [10,20,30]
items.clear()
print(items)