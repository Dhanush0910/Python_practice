#elif examples

mark=int(input('enter your mark: '))
if(mark<35):
    print('Poor')
elif(mark>35 and mark<70):
    print('Average')
elif(mark>=70 and mark<=100):
    print("Good")
else:
    print('Invalid! Enter marks only upto 100')

#Mini calculator

a=int(input('a: '))
b=int(input('b: '))
operation=input('add/sub/mul/div: ')
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("Invalid operation")

#inside the if

score=int(input("Enter your score: "))
if score>=70:
    name=input("Enter your name: ")
    department=input("Enter your department: ")
    print("You are eligible")
else:
    print("You are not eligible")