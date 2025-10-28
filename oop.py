#Python is an object oriented programming language.
#with its properties and methods

#Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

print(MyClass)
 
#Now we can use the class named MyClass to create objects:

class MyClass:
    x = 5
    p1 = MyClass()
    print(p1.x)
    
    #Multiple Objects
class MyClass:
    x = 5
    p1 = MyClass()
    p2 = MyClass()
    p3 = MyClass()
    print(p1.x)
    print(p2.x)
    print(p3.x)
    
#The __init__() Method
#All classes have a built-in method called __init__()
#Create a class named Person, use the __init__() method to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#You can also set default values for parameters in the __init__() method:
#class Person:
  #def __init__(self, name, age = 18):
   # self.name = name
   # self.age = age

#p1 = Person("ahmad",)
#p2 = Person ("faraz" , 28)

#print(p1.name, p1.age)
#print(p1.name , p2.age)

#Create a Person class with multiple parameters:

#class Person: 
       
  #def __init__(self, name, age, city, country):
   # self.name = name
   # self.age = age
   # self.city = city
   # self.country = country

#p1 = Person("Linus", 30, "Oslo", "Norway")

#print(p1.name)
#print(p1.age)
#print(p1.city)
#print(p1.country)

#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Use the Student class to create an object, and then execute the printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

class student (Person):
     pass
x = Person("ahmad", "Doe")
x.printname()

#Add the __init__() function to the Student class:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#Use the super() Function

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("ahmad", "Olsen")
x.printname()

    
       