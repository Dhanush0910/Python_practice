#a text file "example.txt" is created and stored in a folder along with the python code editor
#to perform operations in the file


f = open("c:/Users/dhanu/OneDrive/Desktop/Python practice/27. File-handling/fruits.txt","w")  #opens the fruits.txt file  #"w" is used make it writable as file is automatically is in read format
print(f)   #it will show that the file is in "w" mode

f.write("Grape\n")   #it will over write the fruits file. only Grape exists in the file and others are removed
f.write("Mango\n")

f.close()    #you must close() to save the changes to the file


f=open("c:/Users/dhanu/OneDrive/Desktop/Python practice/27. File-handling/fruits.txt","r+")  #you must open again since the file is closed   #"r+" indicates that it is in both read and write format
print(f)   #it is in r+ format

print(f.read())  #it reads the file and prints the values in the file



#READ method "r" only reads the file and cannot perform write or any operations
#READ AND WRITE method "r+" is used for both reading and writing the file
#WRITE method "w" over writes the file, so
#APPEND method "a" is used to append/add the value to the existing values in the file

f=open("c:/Users/dhanu/OneDrive/Desktop/Python practice/27. File-handling/fruits.txt","a")  #"a" is used append the values to the existing values in the file

f.write("Apple\n")   #the same write method adds the value since "a" is given
f.write("Orange\n")

f.close()

f=open("c:/Users/dhanu/OneDrive/Desktop/Python practice/27. File-handling/fruits.txt","r+")  #need to open again since it is closed, "r+" for readable and writable

print(f.readline())   #it reads only the first line of txt file and prints it

print(f.read())   # it reads the whole file and prints it