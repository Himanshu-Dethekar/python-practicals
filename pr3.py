'''
    Write a program to create a menu with the following options 
    i) TO PERFORM ADDITITON  
    ii)  TO PERFORM SUBTRACTION 
    iii)TO PERFORM MULTIPICATION 
    iv) TO PERFORM DIVISION 
    Accepts users input and perform the operation accordingly. Use functions with arguments. 
'''

def Add(a,b):
    return a + b

def Substract(a,b):
    return a - b

def Multiply(a,b):
    return a * b

def Divide(a,b):
    if b == 0:
        return "cannot divide by 0"
    return a / b

print("____MENU____")

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

choice = int(input("Enter your choice (1,2,3,4)\n"))

if choice == 1:
    print("result:",Add(num1,num2))

elif choice == 2:
    print("result:",Substract(num1,num2))

elif choice == 3:
    print("result:",Multiply(num1,num2))

elif choice == 4:
    print("result:",Divide(num1,num2))

else:
    print("Invalid choice")
    

