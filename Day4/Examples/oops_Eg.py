class person:
    age = 10

    def Hello(self):
        print("Hello")
        return
p = person()
print(person.age)
print(p.age)
print(p.Hello())
print(p.Hello())

class rectangle:
    def __init__(self,length,breadth,cost = 10):
        self.length = length
        self.breadth = breadth
        self.cost = cost

    def area (self):
        return self.length*self.breadth

    def cal_cost(self):
        area = self.area()
        return area*self.cost

r = rectangle(16,12,2010)
print(r.area())
print(r.cal_cost())

class animal:
    def eat(self):
        print("Animal is eating")
class Dog(animal):
    def bark(self):
        print("Dog is barking")

    def eat(self):
        print("Dog is eating")

class cat(animal):
    def bark(self):
        print("Cat is barking")
d = Dog()
d.eat()
d.bark()


class Summation:
    def Sum(self,a,b):
        return a+b
class Multiplication:
    def Mul(self,a,b):
        return a*b

class Derived(Summation,Multiplication):
    def div(self,a,b):
        return a/b
d = Derived()

print(d.Sum(10,20))
print(d.Mul(5,20))
print(d.div(20,2))
print(d.Sum("Hello","World"))
print(d.Mul("Hello",3))
#public
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
s = student("Mahi",10)
print(s.name)

#protected
class student:
    def __init__(self,name,rollno):
        self._name = name
        self._rollno = rollno
s = student("Mahi",10)
print(s._name)

#private
class student:
    def __init__(self,name,rollno):
        self.__name = name
        self.__rollno = rollno
s = student("Mahi",10)
print(s._student__name)
print(s._student__name)



class employee:
   def __init__(self,name):
        self.name = name
   @classmethod
   def detail(cls,name):
       return cls(name)

   @staticmethod
   def emplname(name):
       return name

e =employee("Virat")
print(e.detail("Mahi"))
print(employee.detail("Virat"))
print(employee.emplname("Virat"))