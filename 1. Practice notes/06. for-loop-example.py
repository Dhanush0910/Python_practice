#numbers between a and b

a=int(input("a: "))
b=int(input("b: "))
for i in range(a+1,b):
    print(i)
print("\n")
   
#even numbers between 1 to 10

for i in range(1,11):
    if(i%2==0):
        print(i)
print("\n")
        
#counting them

count=0
for i in range(1,11):
    if(i%2==0):
     count=count+1
print(count,"\n")   

#counting both odd and even

even_count=0
odd_count=0
for i in range(1,11):
    if(i%2==0):
       even_count=even_count+1
    else:
       odd_count=odd_count+1
print("Even: ",even_count)   
print("Odd: ",odd_count)
print("\n")

#counting number divisible by 3 and 5 in 1 to 100

count1=0
for i in range(1,100):
   if(i%3==0 and i%5==0):
      count1=count1+1
print(count1)