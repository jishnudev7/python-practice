num1=int(input("enter the number"))
num2=int(input("enter the second number"))
operation=(input("enter the operation"))
if operation=="+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    if num2!=0:
        print("it is invalid")
    else:
        print(num1/num2)
else:
    print("invalid operation")