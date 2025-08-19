#1. What is module?
#=> A module is file containing Python code(functions,classes, variables)
#Example: math, random are built-in modules.
import math
print(type(math))    #<class 'module'>

#2. How to import a module ?
import math
print(math.sqrt(16))    #4.0

#3.Import specific function from a module
from math import sqrt
print(sqrt(25))   #5.0

#4.Import with alias
import math as m
print(m.ceil(4.2)) 

     #####   Math Module    ####

#6.Use of ceil()
import math
print(math.ceil(4.3))   #5

#7. Use of floor()
print(math.floor(4.7))    #4

#8.Use of fsum()
print(math.fsum([1.2,2.3,3.4]))   #6.9  or  6.8999999999999995

#9.Use of pow()
print(math.pow(2,3))   #8.0

#10. Use of fabs()
print(math.fabs(-4.5))   #4.5

#11. Use of fmod()
print(math.fmod(10,3))   #1.0

#12. Use of sqrt()
print(math.sqrt(81))    #9.0

#13.Use of factorial()
print(math.factorial(5))  #120

#14. Use of cbrt() (Not built-in before 3.11, we use ** (1/3))
print(27**(1/3))    #3.0

#15.Combined use of ceil,sqrt,fabs
print(math.ceil(math.sqrt(math.fabs(-19.4))))     #5

         #####   Random  Module    ####
#16. Use of random()
import random
print(random.random())   #Random float 0-1

#17. Use of randint()
print(random.randint(10,50))   #Random int between 10 and 50

#18. Use of uniform()
print(random.uniform(1.5,6.5))  #Random float

#19. Use of randrange()
print(random.randrange(5,20,3))  #Random number from range

#20. Use of choice()
items = ["apple", "banana","cherry"]
print(random.choice(items))

   #####   DateTime Module    ####
#21.Get current date and time
import datetime
print(datetime.datetime.now())

#22. Use of date.today()
print(datetime.date.today())

#23. Access year,month,day
d = datetime.date.today()
print(d.year,d.month, d.day)

#24. Create specific date
my_date = datetime.date(2025,1,1)
print(my_date)

#25. Difference between two dates
d1 = datetime.date(2025,4,10)
d2 = datetime.date.today()
print((d2-d1).days)

    #####   Time  Module    ####
#26. Get current time in seconds(timestamp)
import time
print(time.time())

#27.Sleep for 2 seconds
print("Start")
time.sleep(1)
print("End after 2 seconds")

#28. Get current time (struct_time)
print(time.localtime())

#29.Format time with strftime()
t = time.localtime()
print(time.strftime("%H:%M:%S",t))

#30.Get readable current time
print(time.ctime())    #Example: "Wed Apr 23  14:22 41 2025"

     #####   Calendar Module    ####
#31.Print full year calendar
import calendar
print(calendar.prcal(2025))

#32. Print month calendar
print(calendar.month(2025,7))

#33.Get weekday of a date
print(calendar.weekday(2025,7,11))   #4 = Friday{ 0 = Monday  & 6 = Sunday}

#34. Check leap year
print(calendar.isleap(2024))   #True

#35.Print all leap years between 2000 and 2025
for year in range(2000,2026):
    if calendar.isleap(year):
        print(year)

     ###  MISCELLANEOUS  ###
#36.Difference between a module and a package.
# MODULE: A .py file with code
# Package: A folder with_init_.py and multiple modules.

#39. Use dir() to inspect module contents
import math
print(dir(math))
