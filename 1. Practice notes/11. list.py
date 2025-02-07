#Python Collections(Arrays):
#list #tuple #set #dictionary


#LIST
#allows duplicate
#any type of data can be stored
#can modify the list item like add, pop, or replace

a=[1,2,3,4,5]
print(a)
print(a[1])   #accessing an element in the list

a.append(6)
print(a)     #adds the element to the end of the list

a.insert(0,10)
print(a)      #insert the element at the 0th position

a[0]=12
print(a)     #replace the 0th element with this number

a.pop()
print(a)    #remove the last element

a.pop(0)
print(a)   #removes the 0th element

b=[6,7,8]
a.extend(b)   #joins the b list with a
print(a)
