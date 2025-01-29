                      #<------<     'Red' is passed into the col
class Fruit:          #|     #|
    def __init__(self,col):  #|      to pass an external parameter "Red", col parameter is called inside the constructor
        self.color=col       #|      getting the col value from the object apple
                             #|
            # >--------------->
            # | 
apple=Fruit("Red")                  #passing the value for color variable as a parameter in the object apple
#generally it is apple=Fruit(apple) so another parameter is used inside init to call another value red. apple=Fruit(apple,"Red")
                             #self                                                                                  self,  col
print(apple.color)




#example2

class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("Name: ",self.name)
        print("Reg No: ",self.regno)

t1=teacher("Ram","001")     #creating object t1 and passing the parameters as value to the name and reg
t2=teacher("Steve","002")

t1.display()
t2.display()




#example3 calculator

class calculator:
    def __init__(self,num1,num2):    #passing 2 parameters num1 and num2
        self.a=num1                  #getting the value of 2 paramters and storing it in 2 variables a and b
        self.b=num2
    def add(self):
        print("add: ",self.a+self.b)  #calling the variables a and b from the constructor
    def sub(self):
        print("sub:",self.a-self.b)
    def mul(self):
        print("mul:",self.a*self.b)
    def div(self):
        print("div:",self.a/self.b)
    
obj=calculator(10,5)       #creating an object for the class calculator and passing the values to the constructor's paramters

obj.add()
obj.sub()
obj.mul()                 #calling the functions
obj.div()