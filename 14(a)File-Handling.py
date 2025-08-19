
# Concept 01.
f = open("durgesh.txt","w")
f.write("Hello bhai ye import  File-Handling se hua hai ,don't be show confuse ")
f.close()

# Concept 02.
f = open("durgesh.txt","r")
r = f.read()
print(r)
f.close()

# Concept 03.
f = open("durgesh.txt","r")
r = f.read()
print(r)
s = str(r)
print(s[-1::-1])
f.close()
#or
f = open("durgesh.txt","r")
r = f.read()
print(r)
print(r[-1::-1])
f.close()

# Concept 04.
f = open("durgesh.txt","a")     #append=kuchh aur uss file mein add or likhna ho tb use kare "a"
l = ["red\n","orange\n","green\n"]
f.writelines(l)
f.close()

# Concept 05.
f = open("durgesh.txt","r")
r = f.readline(1000)           #kitna bhi number kyo naa likh loo oh bas ek hi line ko hi read karega understood baby{readline}
print(r)
f.close()

# Concept 06.
f = open("durgesh.txt","r")
r = f.readlines()              #kitna bhi line kyo na ho file mein sab kuchh read karega in proper manner as mentioned by you {readlines}
for i in r:
    print(i)
    f.close()

# Concept 07.
f = open("durgesh.txt","r")
print(f.read(10))     #btayega ki kitna character  tk read karna hai bhai tujhko bol 
print(f.tell())       #btaayeg ki  present time mein kiss character number pe hai of we can also say in our terms index btaayega
f.seek(17)              #ye jaha mtlb present time mein jish index pr rooka hai wahi se ab continue karega
print(f.read(5))
print(f.tell())
f.seek(30)
print(f.read(4))
print(f.tell())
f.close()

# Concept 08.   Binary Digit ke liye
import pickle
f = open("durgeshbinary.txt","wb")
l = "The quick brown fox jumps over the little lazy dog"
pickle.dump(l,f)
f.close()

import pickle
f = open("durgeshbinary.txt","rb")
r = pickle.load(f)
print(r)
f.close
