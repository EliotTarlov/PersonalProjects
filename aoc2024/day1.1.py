from collections import Counter
with open("./input.txt",'r') as f:
    list1=[]
    list2=Counter()
    
    for line in f:
        line=list(map(int,line.strip().split("   ")))
        list1.append(line[0])
        list2[line[1]]+=1
sum=0
for i in list1:
    sum+=(i*list2[i])
print(sum)
