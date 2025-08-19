#1. What is a dictionary in Python?
# A dictionary is a collection of key-value pairs.
d = {"name":"Alice","age":13}
print(d)

#2.Difference between List,Tuples, and Dictionaries.
#List: Ordered,mutable
lst = [ 1,2,3]
#Tuples: Ordered, immutable
tup = (1,2,3)
#Dictionary: Unordered(until Python 3.7), mutable, key-value pairs.
dic = { "a": 1,"b":2}

#3.Accessing values in a dictionary
d  = {"name":"Bob","age":14}
print(d["name"])    #Bob

#4.Accessing keys in a dictionary
d = { "name": "Bob", "age":14}
print(d.keys())    #dict_keys(['name','age'])

#5. Add a new key-value pair to a dictionary
d = {"name":"Sam"}
d["grade"] = "A"
print(d)

#6.Modify a value in a dictionary
d = { "name":"Sam","grade":"A"}
d["grade"] = "B"
print(d)

#7.Delete a key-value pair using del
d = {"name": "Sam", "grade":"A"}
del d["grade"]
print(d)

#8.Using keys() function 
d = {"x":10,"y":20}
print(list(d.keys()))

#9.Using values() function 
d = {"x":10,"y":20}
print(list(d.values()))

#10. Using items() function
d = {"x":10,"y":20}
print(list(d.items()))

#11.Using pop() to remove a key
d = {"a":1,"b":2}
d.pop("a")
print(d)

#12. Using popitem() to remove the last item
d ={"a":1,"b":2}
d.popitem()
print(d)

#13.Using get() to safely access a value
d = {"a":1}
print(d.get("b","Not found"))
 
#14. Using update() to merge dictionaries
d1 = {"a":1}
d2 = {"b":2}
d1.update(d2)
print(d1)

#15.Using fromkeys() to create a dictionary with default value
keys = ["a","b","c"]
d = dict.fromkeys(keys,0)
print(d)

#16.Check if a key exists in dictionary
d = {"x":1}
print("x" in d)   #True

#17. Loop through a dictionary
d = { "name":"Ann","age":10}
for key, value in d.items():
    print(key,"->", value)

#18.Create a dictionary from a list of keys and a default value
keys = ["math","science"]
d = dict.fromkeys(keys,"Not Graded")
print(d)

#19 Count frequency of letters in word using a dictioary
word = "banana"
freq = {}
for letter in word:
    freq[letter] = freq.get(letter,0) + 1
    print(freq)

#20. Swap keys and values in a dictionary
d  = {"a": 1,"b":2}
swapped = { v :k for k, v in d.items()}
print(swapped)