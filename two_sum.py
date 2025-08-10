num=[2,7,9,22,11]
target=33
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print(i,j)


