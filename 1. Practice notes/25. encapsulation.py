#ENCAPSULATION is used to make a variable private, so that it cannot be accessed by another person 


#PROTECTED variable

class company1():
    def __init__(self):
        self._companyName="Google"   # _ is used to make the variable protected   #_companyName is now protected variable

class a(company1):
    pass

a=company1()      
print(a._companyName)   



#PRIVATE variable

class company():
    def __init__(self):
        self.__companyName="Google"   # __ is used to make the variable private   #__companyName is now private

c1=company()
print(c1.__companyName)   #This gives error, as the PRIVATE variable cannot be accessed outside of its class



#PUBLIC variable is the normal variable that can be accessed anywhere