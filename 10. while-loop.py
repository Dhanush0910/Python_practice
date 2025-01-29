#while loop is used when the range is unknown or not given
#while loop executes when it is true an exits when it is false

i=0
while(i==0):
    print("Yes")   #prints infinite time
    i=1    #false so it stops and exits the loop
print()  #space


#num between 1 and 5

i=1
while(i<6):
    print(i)
    i=i+1
print()

#numbers with 10 gap

i=10
while(i<=200):
    print(i,end=",")
    i=i+10
print()

#reverse order

i=10
while(i>0):  
    print(i,end=",")
    i=i-1
print()


#factorial

n=int(input("Enter a number: "))  # n=5 (any number)
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("The factorial is: ",fact)