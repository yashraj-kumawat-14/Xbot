"""class chocolate:
    name="dairy milk"
    price = 5
    def __init__(self):
        return None
    def details(self):
        print(self.price, self.name)
toffee = chocolate()

class newone(chocolate):
    def yash(self):
        self.details()

a = newone()
a.price
a.yash()

class hello:
    def modify(self):
        self.name = 55
    @staticmethod
    def hel(a, g):
        print(a, g)
a = hello()
a.name= 4
a.modify()
print(a.name)
hello.hel(23, 45)
class fact:
    name = "yashraj"
    @classmethod
    def raj(cls, newname):
        cls.name=newname
a = fact()
print(a.name)
a.name = 4
fact.raj("kemaway")

print(a.name)
print(fact.name)"""

"""class yashraj:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    @classmethod
    def alternate(cls, text):
        return (cls(text.split(".")[0], text.split(".")[1]))

a = yashraj.alternate("ram.14")
print(a.name, a.age)
"""



"""a = [1,3,4]
b = "yashraj"

print(dir(a))
print(dir(b))"""

"""
class hi():
    vay = 55
    def __init__(self):
        self.name = "yashraj"
    def raj(self):
        self.age=4

a = hi()
a.vay=34
print(a.vay)
print(a.__dict__)
print(help(hi))"""


"""class parent:
    def __init__(self):
        print("c of parent")

    def hi(self):
        print("hi feom parent")
class child(parent):
    def __init__(self):
        super().__init__()

    def raj(self):
        super().hi()
a = child()

"""
"""def a(**b):
    print(b)
a(p=1,q="r", s=4.4)"""

class worker:
    def __init__(self,):
        print("hello from c of worker")
    def e(self,):
        print("hello from e of worker")
class engineer:
    def __init__(self,):
        print("hello from c of engineer")
    def e(self,):
        print("hello from e of engineer")
class we(engineer, worker):
    def __init__(self,):
        print("hello from c of we")
    def e(self,):
        print("hello from e of we")

a = we()
print(we.mro())
