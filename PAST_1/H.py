zaikoNum=int(input())
zaiko=[int(x) for x in input().split()]

queryNum = int(input())
queryList=[]
for i in range(queryNum):
    queryList.append(input())

total=0

if zaikoNum == 1:
    z0 = zaiko[0]
    for query in queryList:
        q = [int(x) for x in query.split()]
        if q[0] == 1:
            a=q[2]
            if z0 >= a:
                z0 -= a
                total += a
        else:
            a=q[1]
            if z0 >= a:
                z0 -= a
                total += a
else:
    evenMin=min(zaiko[0::2])
    oddMin=min(zaiko[1::2])
    evenCount=0
    oddCount=0
    for query in queryList:
        q = [int(x) for x in query.split()]
        if q[0] == 1:
            x=q[1]-1
            a=q[2]
            if x%2 == 0:
                modifyZaiko = zaiko[x]-evenCount
            else:
                modifyZaiko = zaiko[x]-oddCount
            if modifyZaiko >= a:
                zaiko[x] -= a
                total += a
                if x%2 == 0:
                    if (modifyZaiko-a) < evenMin:
                        evenMin = modifyZaiko-a
                else:
                    if (modifyZaiko-a) < oddMin:
                        oddMin = modifyZaiko-a
        elif q[0] == 2:
            a=q[1]
            if evenMin >= a:
                evenCount += a
                total += a*int((zaikoNum+1)/2)
                evenMin -= a
        elif q[0] == 3:
            a=q[1]
            if evenMin >= a and oddMin >= a:
                evenCount += a
                oddCount += a
                total += a*int(zaikoNum)
                evenMin -= a
                oddMin -= a
print(total)
