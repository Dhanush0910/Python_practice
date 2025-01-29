#CONSTRUCTOR
#A constructor is a unique function that gets called automatically when an object is created for the class
#main purpose of constructor is to initialize or assign values to the contents inside the class

#SELF keyword
#self keyword is used to denote the current object


class hello:
    def __init__(self):  #__init__(self) is the constructor which is an in-built function that is called automatically when an object is created
        print("Hello!")
obj=hello()  #object will automatically call the constructor 


#eaxample

class laptop:    
    def __init__(self):    #constructor which is an in-built function that is called automatically when an object is created
        self.ram=""        #initializing the variable with an empty string
        self.processor=""
    def display(self):
        print("ram: ",self.ram)
        print("processor: ",self.processor)
    
hp=laptop()  #creating an object which automatically calls the constructor inside the class
dell=laptop()

hp.ram="8gb"  #providing the value to the variables ram of the object hp
hp.processor="i5"

dell.ram="16gb"
dell.processor="i7"

hp.display()  #calling the function
#generally taken by the system as "hp.display(hp)" which represents the self.ram as hp.ram

dell.display()  #the dell is a parameter passed to the fuction display 
#the self parameter represents the current object which is dell here so it is dell.ram



#empty class

class nothing:
    pass        #this will provide an empty class without error