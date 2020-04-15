n = int(input())

nList=[]
aList=[]
for i in range(n):
    nList.append(i+1)
    aList.append(int(input()))

nsum = sum(nList)
asum = sum(aList)

if nsum == asum:
    print("Correct")
else:
    x = list(set(nList) - set(aList))[0]
    y = x + (asum - nsum)
    print(y,x)
