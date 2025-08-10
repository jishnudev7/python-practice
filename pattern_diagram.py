rows=int(input("enter the number of rows"))
for i in range(rows):
    for s in range(0,rows-i-1):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()