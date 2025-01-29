def valueof():
    return "Hello"

print(valueof())  #Hello is stored inside valueof() function and print() diplays the Hello
#or

a=valueof()
print(a)



#validating username and password

s_username="dhanush"
s_password="123"

username=input("Enter username: ")
password=input("Enter password: ")

def validate():
    if(username==s_username and password==s_password):
        return True
    else:
        return False

a=validate()
print(a)



# (a+b)*c

a=int(input("Enter a: "))
b=int(input("Enter b: "))
def add():
    return a+b

c=int(input("Enter c: "))

operation=add()*c
print(operation)

#or

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
def addition(x,y):
    return x+y

added=addition(a,b)
output=added*c
print(output)