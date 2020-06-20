thisdict = {"country":"India",
            "fruit":"Apple",
            "vegetable":"Carrot"}

print(thisdict)
print(type(thisdict))

emptydict = {}
print(type(emptydict))

#Retreving Values from Dict

print(thisdict["fruit"])
x = thisdict.get("vegetable")
print(x)

thisdict = {"country":"India",
            "fruit":"Mango",
            "vegetable":"Carrot"}
print(thisdict)

fruits = ["apple","mango"]
print(fruits[0])
#print(thisdict[2])
#Loops

#Keys
for t in thisdict:
    print(t)
#values
for t in thisdict:
    print(thisdict[t])


#Keys
for t in thisdict.keys():
    print(t)
#values
for t in thisdict.values():
    print(t)
#both keys and values

for t in thisdict.items():
    print(t)
    if "vegetable" in t:
        print("present")

d = {"01":"Arun",
     "02":"Balaji",
     "03":"Dinesh"}

print(d)
newstudent = d.copy()
print (newstudent)
d.clear()
print (d)

x = {1,2,3}
print (x)
print(type(x))
x.clear()
print(x)

y = {}
print(type(y))
z = set()
print(type(z))

cric = {"India":"Virat",
        "Aus":"Smith",
        "SA":"ABD"}
print(cric)
cric.pop("Aus")
print(cric)
cric.popitem() # it will elimate the last inserted value
print(cric)

cric = {"India":"Virat",
        "Aus":"Smith",
        "SA":"ABD"}

c= cric.setdefault("NZ","Kane")
print(cric)

cric.update({"pak":"Babar"})
print(cric)
cric.update({ "Aus":"Warner"})
print(cric)
cric.update({"aus":"starc"})


def rec(x):
    if x == 1:
        return 1
    else:
        return (x*(rec(x-1)))

print(rec(4))
