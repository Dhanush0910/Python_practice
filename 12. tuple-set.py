#TUPLE

#allows duplicate
#any type of data can be stored
#cannot modify the tuple item like add, pop, or replace 
#represented as ()

a=(1,2,3,4,5)
print(a)     #cannot modify the elements

b=list(a)    #can be changed into list for modifying (casting)
print(b)     

b.append(6)  #list methods can be performed
print(b)

print()  #line space



#SETS

#does not allow duplicates
#any type of data can be stored
#sets are unordered
#cannot modify items but can add(), update(), pop() an remove()

c={1,2,3,4,8,5,1,3,4}  #prints in unorder
print(c)      #duplicate elements are not printed

c.add(7)
print(c)   #adds 7 in its another order

c.pop()
print(c)   #removes any number inside the set
 
c.remove(4) #removes number 4
print(c)