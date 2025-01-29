#Three types of errors:

# 1. compile time error = syntax error which is occured at the time of compiling and gives error soon after you run the program.  Eg. prinnt()

# 2. Logical error = error in logics like mathematical errors.  Eg. a=10  b=20  print(a+a)

# 3. Run time error = program runs properly, and after entering the input values, it throws error which is called the Run-time error that is occuring during the run time
# Eg. a=int(input())  b=int(input())  print(a+b)    #O/P: a=10  b=ten  Error/   #if the user enters the details wrong it throws error. It needs to be handled

#compile-time and logical errors cannot be handled, it is a manual error that requires human carefullness


#EXCEPTION HANDLING is to handle the Run-time errors in the program


try:
    a=int(input("a: "))
    b=int(input("b: "))
    c=input()
    print(c/a)     #division only works on integers not strings which throws TypeError


except TypeError as e:   #to handle the TypeError     
    print("Type Error",e)

except ValueError as e:      #to handle ValueError if the user enters any string in integer a
    print("Value Error",e)

except Exception:            #handles if any other error than the type or value error occurs 
    print("Something Wrong")  #prints this if any other error occurs


finally:             #finally block executes even after the error. #it executes surely even if it error occurs or not
    print("Done")


#there are many errors like NameError and more