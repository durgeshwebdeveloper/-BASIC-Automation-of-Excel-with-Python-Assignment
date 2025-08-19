     #### TUPLE BASICS & DIFFERENCES

#1. Create a tuple with 5 integers and print it.
t = (10,20,30,40,50)
print(t)

#2 Why is a tuple called an immutable data type? Show with example.
t = (1,2,3)
#t[1] = 5   #This will raise a TypeError
print("Tuples cannot be changed once created.")

#3.Diffrence between list,tuple,and string.
my_list = [1,2,3]
my_tuple = (1,2,3)
my_string = "123"
print(type(my_list),type(my_tuple),type(my_string))

##ACCESSING AND ITERATING
#4.Access the first and last element of a tuple.
t = ("apple","banana","cherry")
print((t[0]))   #apple
print(t[-1])    #cherry

#5.Iterate through a tuple using a for loop.
t = ( 10,20,30)
for i in t:
    print(t)
#6.Check if an item exists in a tuple.
t = (10,20,30)
print(20 in t)

   ## TUPLE OPERATIONS 
#7. Concatenate two tuples.
a = (1,2)
b = (3,4)
c = a+b
print(c)

#8.Repeat a tuple 3 times.
t = (5,6)
print(t*3) 

#9.Find the index of an item in a tuple.
t = (10,20,30)
print(t.index(20))

#10. Count how many times an element appears.
t = (1,2,2,3,2)
print(t.count(2))

   # CONVERSION BETWEEN LIST AND TUPLE
#11.Convert a list into a tuple.
l = [1,2,3]
t = tuple(l)
print(t)

#12.Convert a tuple into a list.
t = (4,5,6)
l = list(t)
print(l)

#13.Create an empty tuple and check its type.
t = ()
print(type(t))

#14.Create a single-element tuple.
t = (5,)
print(t,type(t))

    #### AGGREGATION FUNCTIONS ON TUPLES
#15.Use sum() to add all elements in a tuple.
t = (10,20,30)
print(sum)

#16.Find the mas() value in a tuple.
t = (4,9,1,6)
print(max(t))

#17. Find the min() value in a tuple.
t = (4,9,1,6)
print(min(t))

#18.Use len() to find tne number of elements.
t = (1,2,3,4)
print(len(t))

  ## APPLICATION EXAMPLES

#19. Create tuple of months and print them.
months = ("Jan","Feb","Mar","Apr")
for m in months:
    print(m)
#20. Convert a tuple to list , modify it, and convert back.
t = (1,2,3)
l = list(t)
l[1] = 5
t = tuple(l)
print(t)