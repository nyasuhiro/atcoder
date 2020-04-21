n,m = map(int,input().split())
aList = [int(x) for x in input().split()]

aList.sort(reverse=True)
total = sum(aList)
if aList[m-1]*4*m >= total:
    print('Yes')
else:
    print('No')
