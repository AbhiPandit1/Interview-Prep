# OOPS

#Class
# A class is a a blueprint for object .It defines the attribute meathod and variables that the object created from class will have . A class doest contain original data whereas serve as template

Class Abhishek:
       name="Abhishek" # Attribute it will initialise in every instance of class
        def __init__(self):
        # This is constructor it is used to initialize attribute of an object

        def anyFunction():
        # This is a function inside a class which is used to initialse meathod

## __init__ 
 it is a special meathod in python is constructor it is initialise every time the object is initialise using the class
 it is used to initialize attribute for the new object

## self keyword
it is a  special keywod which is used to refer current instance of class. it allows access to current attribute and meathods of object



### Principles of OOPS
There are four principles and pillar of OOPS you can say

Encapsulation(get set method define krne ke lie)
Abstraction(base methode define krenge abstraction me and pass krdenge aage )
Inheritance(baap bete k rista )
Polyporphism(ek meathod ke different class me different roop)


### Encapsulation
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def getBalance(self):   # example of get function
        return self.balance
    
    def deposit(self,depositBalance): ## Example of set function
        self.balance+=self.deposit
        return self.balance 

### Encapsulation is uses to stop giving direct access to some of the property that we want to keep hidden


### Abstraction

class Shape:
      def __int__(self):
          pass
      def shape(self):
          pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def shape(self):
      return self.radius*radius

## This is and example of abstraction we have made a interface circle will have all the methode that are in shape and we have to assign a mathod to it we we not it will raise a error in our clasee


### Inheritance

class Animal:
     def __init__(self,breed):
        self.breed=breed
     def sound(self,)
### polyporphism
j