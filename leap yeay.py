year=int(input("enter the year you want ot check"))
# Check the leap year condition
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):

    print("it is a leap year")
else:
    print("it is not a leap year")