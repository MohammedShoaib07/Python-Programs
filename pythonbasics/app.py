## WRITE A PROGRAM TO FIND LARGEST AND 2ND LARGEST NUMBER AMONG GIVEN 3 NUMBERS

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))

if num1>num2 and num1>num3:
    print("The largest number is : ",num1)
    if num2>num3:
        print("The second largest number is : ",num2)
    else:
        print("The second largest number is : ",num3)