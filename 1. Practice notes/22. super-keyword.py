#SUPER keyword is used to access the element from the parent class

class a():
    def __init__(self):
        print('A')
    def display(self):
        print('a')

class b(a):
    def __init__(self):   #constructor is called automatically as soon as an object is created
        print('B')
    def display(self):
        print("b")
    
obj1=b()    #generally it prints B, but if class b is without the constructor, it moves to its parent class a

print()  #space



#super keyword

class a():
    def __init__(self):
        print('A')
    def display(self):
        print('a')

class b(a):                #obj2 calls this class b
    def __init__(self):     #constructor is called as soon as obj is created
        super().__init__()    #init() of the parent class a is called by the super(), where it prints A
        print('B')            #it prints B
    def display(self):
        print("b")

obj2=b()     #the output will be A and B


print()  #space



#for multiple inheritance

class a():
    def __init__(self):
        print('A')
    def display(self):
        print('a')

class b():                
    def __init__(self):     
        super().__init__()    
        print('B')            
    def display(self):
        print("b")

class c(a,b):              #obj3 calls this class c
    def __init__(self):      #constructor is called as soon as obj is created
        super().__init__()    #init() of the class A is called first as it is written first and it prints A
        print('C')           #it prints C
    def display(self):
        print('c class')

obj3=c()     #the output will be A and C

print()  #space



#playing with super()

class a():
    def __init__(self):
        print('A')
    def display(self):
        print('a')

class b():                  #the super() in class C calls this class b 
    def __init__(self):      #constructor is called as soon as obj is created
        super().__init__()    #init() of its parent class A is called where it prints A
        print('B')            #then it prints B
    def display(self):
        print("b")

class c(b,a):              #obj3 calls this class c
    def __init__(self):      #constructor is called as soon as obj is created
        super().__init__()    #init() of the class B is called first as it is written first and in class B, see in B
        print('C')           #then it prints C
    def display(self):
        print('c class')

obj4=c()     #the output will be A, B and C