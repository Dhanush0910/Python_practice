#if-else examples

#binary operators- and,or,not

num=int(input('enter a number: '))
if(num % 3 == 0 and num % 5 == 0):
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by 3 and 5")

#odd or even

num1=int(input("enter a num: "))
if(num1 % 2 == 0):
    print("even number")
else:
    print("odd number")
