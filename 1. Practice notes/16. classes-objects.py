class laptop:     #class
    price = 0       #variables with 0 value for accessing and changing later 
    processor=""    #variables with empty string for accessing and changing later
    RAM=""

    def purchase(self):   #a function  #self is must when creating a function inside the class
        print("Purchace confimed")
    def not_purchase(self):
        print("Not purchased")
    
dell=laptop()    #object dell which gains the access to the class laptop() and the contents inside the class
hp=laptop()      
lenova=laptop()

dell.price="40000"    #providing value to the variable of the object
dell.processor="intel core"
dell.RAM="16gb"

hp.price="50000"   
hp.processor="ryzen"
hp.RAM="16gb"

print("dell price: ",dell.price)
print("dell processor: ",dell.processor)
print("dell RAM: ",dell.RAM)

dell.purchase()    #calling the fuction inside the class for the object dell
print()  #a space

print("HP price: ",hp.price)
print("HP processor: ",hp.processor)
print("HP RAM: ",hp.RAM)

hp.not_purchase()