num=[2,5,8,9,9]
duplicate={}
for i in num:
    if i not in duplicate:
        duplicate[i]=1
    else:
        duplicate[i]+=1

for num,count in duplicate.items():
    if count>1:
        print(num,count)
