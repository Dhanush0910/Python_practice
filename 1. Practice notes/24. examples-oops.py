#example 1  overriding

class Shape():
    def area(self):
        return 0
    
class Rectangle(Shape):
    def area(self):      #area() function in shape() class is overriden here
        l=10
        b=2
        return l*b
    
s1=Shape()
print(s1.area())   # since area() has return, print() is used to display the value in return, else it does not print anything as the whole function area() becomes 0, the value it returns

r1=Rectangle()
print(r1.area())  #the area() function is overriden


print()



#example 2  super keyword

class person():
    def __init__(self,name):   
        self.name=name

class student(person):
    def __init__(self,name,grade):   #setting the name parameter from its parent class person
        super().__init__(name)      #super() is used to access that self.name from its parent
        self.grade=grade
    
    def display(self):
        print("Name:",self.name)
        print("Grade:",self.grade)

s1=student("Dhanush","A")
s1.display()

print()  #space



#example3   overriding

class vehicle():
    def start(self):
        print("Vehicle started")

class car(vehicle):
    def start(self):
        print("Car started")

c1=car()
c1.start()

print()  #space



#example 4   super keyword and inheritance

class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department

    def display(self):
        print(self.name, self.salary, self.department)

m1=Manager("Tony","2000000","Pilanthrophist")
m1.display()