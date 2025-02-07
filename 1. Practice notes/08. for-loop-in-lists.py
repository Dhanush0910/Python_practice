sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
print("\n")


#get 5 input numbers and display their sum and average

a=[]  #list[]
for i in range(5):
    num=int(input("Enter num "+str(i+1)+str(": ")))     #integer can be concatenated with string with casting str()      # i is used to display the number      # i+1 is used to start from 1 as normally it starts from 0 
    a.append(num)                                   #append adds the num to the end of the list
print(a)                                          #the list with 5 num is printed
            
sum=0
for i in a:                #for i in list a
    sum = sum + i          #adds sum and the in list to sum
print("Their sum is: ",sum)

count=0
for i in a:
    count=count+1          #adds 1 to each time of loop
avg=sum/count
print("Their average is: ",avg)
#or
average=sum/len(a)
print("the average is: ",average)


#to display n terms of natural numbers and their sum

b=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):          #n+1 contains the numbers upto n
    b.append(i)
print(b)

sum1=0
for i in b:
    sum1=sum1+i
print("The sum is: ",sum1)


#To display the cube of the numbers upto an integer

c=[]
num1=int(input("Enter a number: "))
for i in range(1,num1+1):
    c.append(i)
    cube=i**3    #cube= i*i*i
    print("The number is: ",i," and its cube is: ",cube)  #making this inside the loop to print the state everytime for each number

#or

num2=int(input("Enter a number: "))     #without using list
for i in range(1, num2 + 1):
    cube2=i**3
    print("The number is: ",i," and its cube is: ",cube2)