n=int(input())

aList=[]
for i in range(n):
    aList.append(int(input()))

for i in range(len(aList)-1):
    sabun=aList[i+1]-aList[i]
    if sabun == 0:
        print("stay")
    elif sabun < 0:
        print("down",abs(sabun))
    else:
        print("up",sabun)
