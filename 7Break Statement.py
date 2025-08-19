       ### BREAK STATEMENT ###
#1.Stop the loop when number equals 5.
for i in range (1,11):
    if i == 5:
        break
    print(i)

#2.Break in a while loop when input is "exit".
while True:
    text = input("Enter text:")
    if text == "exit":
        break
    print("You entered : ", text)

#3.Break when a specific item is found in a list.
fruits = ["apple", "banana", "cherrry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)
    

#4. Find first even number and break the loop.
numbers = [1,3,5,6,7,8]
for num in numbers:
    if num % 2 == 0:
        print("First even: ", num)
        break
#5.Search for a numbers in a list using break.
nums = [12,34,55,78]
target = 55
for n in nums:
    if n == target:
        print("Found!")
        break
    else:
        print("Not Found")

       #### CONTINUE STATEMENT ###
#6.Print only even numbers from 1 to 10.
for i in range (1,11):
    if i % 2 != 0:
        continue
    print(i)

#7. Skip printing vowels in a string.
text = "hello World"
for char in text:
    if char in "aeiou":
        continue
    print(char, end =" ")

#8. Print numbers 1 to 10, skip 5.
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#9. print numbers from list,skip negative ones.
nums = [3,-1,7,-5,10]
for num in nums:
    if num < 0 :
        continue
    print(num)

#10. Sum only positive numbers from list.
nums = [-3,5,-7,4]
total = 0
for  num in nums:
    if num < 0:
        continue
    total += num
    print("Sum: ", total)

    ##### PASS STATEMENT  #####
#11.Write a while loop that does nothing (Placeholder).
for i in range(5):
    pass

#12. Pass in an empty function.
def future_function():
    pass

#13.Use pass in an unimplemented if block.
x = 10
if x > 0:
    pass
else:
    print("Negative")

#14. Use pass inside class definition.
class MyClass:
    pass

#15. Write a loop with condition not yet defined.
for i in range(10):
    if i % 2 == 0:
        pass   #To be implemented later
    else:
        print(i)

#16. Demonstrate break and continue in the same loop.
for i in range(1,10):
    if i == 3:
        continue 
    if i == 7:
        break
    print(i)

#17. Explain difference: break v/s continue:
   #break the loop
    for i in range(5):
        if i == 2:
            break
        print(i)
      
    #continue skips the current iteration
for i in range(5):
    if i == 2 :
        continue
    print(i)  

#18. Demonstrate pass v/s continue.
for i in range(3):
    if i == 1:
        pass     #does nothing
    print(i)

#19. Use break in infinite while loop.
count = 0
while True:
    print(count)
    count += 1
    if count ==3:
        break

#20. Skip odd numbers, break at number divisible by 6.
for i in range(1,20):
    if i % 2 != 0:
        continue
    if i % 6 == 0:
        break
    print(i)