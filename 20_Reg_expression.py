'''#1.Import the re module and check if a string contains only digits.
import re 
text = "123456"
print(re.fullmatch(r"\d+",text))   #True

#2. Use match() to check if string starts with "Hello"
import re 
result = re.match("Hello", "Hello World")
print(bool(result))  #True

#3.Use search() to find "World" anywhere
import re 
result = re.search("World", "Say Hello World!")
print(result.group() if result else "Not Found")  #True   World 

#4. Difference between match() and search()
import re 
text = "Python is powerful"
print(re.match("powerful", text))   #None
print(re.search("powerful", text))  # Found

#5.Validate an email address using regex.
import re 
email = "test@example.com"
pattern  = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(bool(re.match(pattern, email)))   #True

#6.Find all digits in a string  using findall()
import re  
text = "Phone: 9026407956,  Age: 23"
print(re.findall(r"\d+", text))   #Output: ['9026407956', '23']

#7.Use sub() to replace all whitespaces with dashes
import re
text = "Hello World from Python"
print(re.sub(r"\s", "-", text))  #Output:Hello-World-from-Python

#8.Use split() to tokenize a string.
import re  
text = "apple, orange ; banana|grapes"
print(re.split(r"[,:]\s*", text))  #Output: ['apple', 'orange ; banana|grapes']

#9.Check if string starts with uppercase using match()
import re  
text = "Python"
print(bool(re.match(r"[A-Z]", text)))   # Output: True

#10. Match string with exactly 3 letters followed by 2 digits.
import re  
text = "abc12"
print(bool(re.fullmatch(r"[A-Za-z]{3}\d{2}",text)))   #Output: True

#11.Extract hashtags from a sentence.
import re  
text = "Loving the #sunshine and #vacation vibes!"
print(re.findall(r"#\w+", text))    # Output: ['#sunshine', '#vacation']

# 12. Usind regex with re.IGNORECASE modifier
import re 
text = "python is fun"
print(bool(re.match("PYTHON", text, re.IGNORECASE)))   #Output:  True

# 13. Context-Free Grammar (CFG) simulatioin: match subject-verb
import re  
sent = "He eats"
pattern = r"(He|She|It) (eats|runs|walks)"
print(bool(re.fullmatch(pattern, sent)))  # Output: True

# 14. Match valid Phone Number (10 digits)
import re 
phone = "9026407956"
print(bool(re.fullmatch(r"\d{10}", phone)))  #Output: True'''

# 15.Match only words with 4 to 6 letters 
import re  
words = "apple bat elephant tiger"
print(re.findall(r"\b\w{4,6}\b", words))  #Output: ['apple', 'tiger']

# 16. Practical : validate password (min 6 char, 1 digit, 1 upper)
import re  
pwd = "Pass123"
pattern = r"^(?=.*[A-Z])(?=.*\d).{6,}$"
print(bool(re.match(pattern, pwd)))    # Output: True

# 17. Use lambda with map to convert string list to uppercase 
words = ["apple", "banana", "mango"]
print(list(map(lambda w: w.upper(),words)))  #Output: ['APPLE', 'BANANA', 'MANGO']

#18. Use lambda with filter to find even numbers 
nums = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x : x % 2 == 0, nums  )))   #Output: [2, 4, 6, 8]

#19. Replace all numbers with # using regex 
import re  
text = "Room 42, Floors 8"
print(re.sub(r"\d+", "#", text))   # Output:Room #, Floors #

#20. Count occurences of words using regex 
import re  
from collections import Counter 
text = "cat dog cat mouse dog dog "
words  = re.findall(r"\w+", text)
print(Counter(words))  #Output: Counter({'dog': 3, 'cat': 2, 'mouse': 1})