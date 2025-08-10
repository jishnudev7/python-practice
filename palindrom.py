num=int(input("enter the first number"))
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*0 + digit
    num=num//10
    print(reversed_num, end="")
