n = int(input())
aList=[]
aList += [int(x) for x in input().split()]
bukaList=[0]*n
for i in range(n-1):
    bukaList[aList[i]-1]+=1
print(*bukaList,sep='\n')
