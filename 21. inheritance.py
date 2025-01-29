#INHERITANCE:

# SINGLE INHERITANCE is a class calling a function from another class

class dad():
    def phone(self):
        print("Dad's phone")

class son(dad):          #single inheritance   #accessing dad class inside son
    def laptop(self):
        print("Son's laptop")

monish=son()     #an object created that accesses the son class

monish.laptop()
monish.phone()   #calls the phone() function that belongs to another class dad()


print()   #space




#MULTIPLE INHERITANCE is calling multiple classes from another class

class father():
    def phone1(self):
        print("Father's phone")

class mother():
    def sweet1(self):
        print("Mother's sweet")

class daughter(father,mother):          #multiple inheritance   #accessing multiple classes like father and mother class inside daughter
    def laptop1(self):
        print("Daughter's laptop")

kelly=daughter()     #an object created that accesses the daughteer class

kelly.laptop1()
kelly.phone1()   #calls the phone1() function that belongs to another class father()
kelly.sweet1()   #calls the sweet1() function that belongs to another class mother()


print()   #space




#MULTI LEVEL INHERITANCE is multiple classes accessing functions from multiple other classes so that they are interlinked

class grandpa():
    def phone2(self):
        print("granda phone")

class daddy(grandpa):       #grandpa class is accessable by daddy class
    def money(self):
        print("daddy money")

class sonn(daddy):           #daddy class is accessable by sonn class by which both grandpa also accessable
    def laptop3(self):
        print("son laptop")

moni=sonn()

moni.laptop3() 
moni.money()
moni.phone2()   #all the functions from another classes are accessable by sonn since all are connected


print()



#HIERARCHICAL INHERITANCE is multiple classes accessing one class

class dad1():
    def money1(self):
        print("dad's money")

class son1(dad1):
    pass

class son2(dad1):    #all the son classes are linked with dad class
    pass

class son3(dad1):
    pass

s2=son2()

s2.money1()    #money() function in dad1 class can be called any son class since all sons are connected to dad1


print()  #space




#HYBRID INHERITANCE is all the single, multiple, multi level and hierarchical interheritance exists together

class dad2():
    def money2(self):
        print("dads money")

class land():
    def important(self):
        print("importand land")

class son4(dad2,land):       #multiple inheritance where one class access multiple classes
    pass

class son5(dad2):        #hierarchical inheritance where all sons access the dad
    pass

class son6(dad2):
    pass

ram=son4()    #obj that gets access to son4
steve=son5()

ram.money2() 
ram.important()   #different inheritances takes place together which is called hybrid interitance

steve.money2()