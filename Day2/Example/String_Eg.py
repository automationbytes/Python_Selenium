#examples
ab = "Hello World"
print(type(ab))
print(ab)


cd = 'Hello World'
print(type(cd))
print(cd)
singlechar = 'C'
print(type(singlechar))

#Multiple Line declaration
para = '''This is an example of
multiline string
and it will be starts 
and end with 3ple quotes'''
print(para)

#Length
name = "Selenium"
print(len(name))
print(len(para))

#indexing
fruit = "Orange"
print(fruit[1]) # return r it will starts with zeroth index
print(fruit[-5])

#slicing
fr = "Orange"
print(fr[1:4])
print(fr[2:])
print(fr[:4])
print(fr[-5:-2])
print(fr[-5:])

#Strip - Elimate the spaces

a = "         India is my country         "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#lower - to print in lower case
b = "Hello world"
print(b.lower())
#Upper - to print in upper case
print(b.upper())
#Captialise - captialize the first word of the string
c = "pride of india"
print(c.capitalize())
#title - it will captialize first letter of each word
print(c.title())

any = c.replace("p","")
print(any)

sp = c.split(" ")
print(sp)
print(sp[-1])

print("india" not in c)

#Concatenation
a = "Hi"
b = "How"
q = "are"
r = "you"
print(a+b+q+r)

c = 3
d = "sha"
e = "python"
print(c,d)
print(format(c)+d+e)

print("India\nAus")

a = "Selenium"
print(a.count('e'))
print(a.endswith('m'))
print(a.index('e'))

print(a[::-1])

sel = "Selenium"
for s in sel:
    print (s)

#reverse a string using loop
sel = "Selenium"
s1= ""
for s in sel:
    s1 = s+s1
    print (s1)
    print(type(s))

email = "google@gmail.com,raghu@ymail.com"
emailnew = email.split("@")
print(emailnew)

for s in range(1,10,1):
    print(type(s))
    print(s)
