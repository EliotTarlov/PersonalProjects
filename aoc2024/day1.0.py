with open("./input.txt",'r') as f:
    list1=[]
    list2=[]
    
    for line in f:
        line=list(map(int,line.strip().split("   ")))
        list1.append(line[0])
        list2.append(line[1])
    list1.sort()
    list2.sort()
sum=0
for i in range(len(list1)):
    sum+=abs(list1[i]-list2[i])
print(sum)
