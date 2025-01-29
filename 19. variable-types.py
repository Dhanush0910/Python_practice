#Two types of variables: 

# 1. class variables
# 2. instance variables

class phone:
    chargertype="C-TYPE"  #class variable  #c-type is common for all the phone so, it is given as class variable
    def __init__(self,brand,price):  
        self.brand=brand   #intance variable that differs for different phone
        self.price=price   #passing the value of price from the parameter price for the self.price variable

    def display(self):
        print("Brand:",self.brand)    #calling the intance variable self.brand
        print("Price:",self.price)    
        print("Charger type:",self.chargertype)   #calling the class variable self.chargertype

samsung=phone("Samsung","20000")  #creating an object samsung and passing the values
redmi=phone("Redmi","15000")

samsung.display()   #calling the display function for the samsung object 
redmi.display()