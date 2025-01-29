for i in range(1,5):      #contains 1,2,3,4
    for j in range(1,3):  #contains 1,2
        print(i,j,"Apple") 
        #first go through the i loop which is 1 and it moves to the j which is 1 and again checks in the j which is 2 
        # and then moves to i again which is 2 and comes to the j which is 1 followed by 2 and again to i 3.... upto the limit of i
print() 

#loop inside loop

for i in range(1,3):
    print("Week:",i)     #prints 1,2
    for j in range(1,4):
        print("Day:",j)   #prints 1,2,3
print() #moves to next line 


#pattern printing

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

# * pattern

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()