#POLYMORPHISM is using the same function in different types
#The difference is mosty in the data types and in the parameters passed

def add(a,b,c=0):   #c value is given inside the parameter
    print(a+b+c)

add(1,2)    #without the c=0, this will print error as c is not defined. but here, the c is 0
add(1,2,3)   #this will make c=3
#the same add() function returning two different types of values is called polymorphism

print()  #line space




#example

class Animal():       #parent class/ base class
    def sound(self):  #funtion/method
        print("Animal makes sound")

class Dog(Animal) :    #child class/ derived class that inherits from animal
    def sound(self):    #METHOD OVERRIDING
        print("Dog barks")  #it over writes the sound function to print "Dog barks"

class Bird(Animal):
    def sound(self):
        print("Birds sing")  #it overrides the sound function to "Birds sing"

a1=Animal()
a1.sound()   #prints "Animal makes sound"

d1=Dog()
d1.sound()   #prints "Dog barks"

b1=Bird()
b1.sound()   #prints "Birds sing"

#same sound() function is used in different types is called POLYMORPHISM

#over writing the value of same function is called METHOD OVERRIDING