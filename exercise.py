#reverse a string (while loop)

s=input("Enter a word: ")
reverse_string=""  #an empty variable
i=len(s)-1      #last index of a string where len(s) is the length of the string
                #for eg. hello has length 5, the index start from 0, so it is 0 to 4 where 4 is the last index, so it is len(string) - 1 gives 4

while(i>=0):    #0 is the last value since we start form end
    reverse_string = reverse_string + s[i]   #adding the index value in s to the empty variable
    i-=1   #assignment operator which denotes i = i - 1

print(reverse_string)



#reverse a string (for loop)

n=str(input("Enter a String: "))
rev=""
    
                 #(start, stop, step)
for index in range(len(n)-1, -1, -1):    #len(n)-1 is the last value, -1 is the value before to stop which means it stops at 0, -1 is decrementing 1 value
    rev += n[index]

print(rev)



#list comprehensions

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
n = int(input("n:"))   #(constraint):sum of indeces i,j,k should not be equal to n
result = [[i,j,k] for i in range(x+1) for j in range(y+1) #it is the shorter form of: result=[]  for in range(x+1)  for j..  for k..  if(x+y+z!=n):
for k in range(z+1) if(i+j+k != n)]                                                                   #result.append([i,j,k])

print(result)