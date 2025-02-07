#Three types of methods:

#1. instance method
#2. class method
#3. static method

class laptop:
    chargertype="C TYPE" 

    def __init__(self):   #instance method is called with self
        self.brand=""      
        self.price=10000
    
    def setPrice(self,price):    #self is used as the parameter for the INSTANCE METHOD which generally takes object as the self
        self.price=price

    def getPrice(self):
        print(self.price)


    @classmethod                     #class method is activated by @classmethod
    def changeChargerType(cls):      #cls is passed as a parameter for CLASS METHOD
        cls.chargertype="B TYPE"
        print("Charger type changed to B")


    @staticmethod                 #static method activated by @staticmethod
    def info():                         #normal function that does not require any self or cls parameters
        print("This is laptop class")  


hp=laptop()      #object is created for laptop class
hp.getPrice()    #getprice() gets the value from init which is 10000

hp.setPrice(20000)  #the price value is changed to 20000
hp.getPrice()       #the changed value 20000 is printed

hp.changeChargerType()   #class method is called where hp passed into cls by using @classmethod

hp.info()   #static method is called