##rows =int(input("enter the number of rows:" ))
##for i in range(0,rows):
    ##for j in range(0,rows-i-1):
      ##  print(end= " ")
    ##      print("*",end=" ")
##    print()
rows=int(input("enter the number of rows"))
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(end=" ")
    for s in range(i):
        print("*",end=" ")
    print()