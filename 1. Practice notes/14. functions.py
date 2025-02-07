def add():   #defining a function named add
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    print(a+b)
add()        #functions only return the operations inside when it is called


#using parameter/arguements

         #paramter
def painter(msg):  
    print("Message is: ",msg)

painter("Hi painter")  #the content inside the function is stored as the parameter msg
painter("How are you")


#finding even or odd

def evenorodd(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")

num=int(input("Enter a number: "))
evenorodd(num)   #num will be assigned to the parameter n 


#printing range between a and b

def printrange(x,y):
    for i in range(x,y):
        print(i)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
printrange(a,b)   #value of a,b is assigned to the x,y