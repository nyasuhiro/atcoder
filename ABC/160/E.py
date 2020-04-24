X,Y,A,B,C = map(int,input().split())
pList = [int(x) for x in input().split()]
qList = [int(x) for x in input().split()]
rList = [int(x) for x in input().split()]

pList.sort(reverse=True)
qList.sort(reverse=True)
rList.sort(reverse=True)

stackX=[]
stackY=[]
stackR=[]

for i in range(X):
    stackX.append(pList[i])

for i in range(Y):
    stackY.append(qList[i])

for i in range(C):
    if len(stackX)>0:
        x = stackX[-1]
    else:
        x = pow(10,10)

    if len(stackY)>0:
        y = stackY[-1]
    else:
        y = pow(10,10)

    r = rList[i]

    if r <= x and r <= y:
        break
    elif x < y:
        stackX.pop()
        stackR.append(r)
    else:
        stackY.pop()
        stackR.append(r)
print(sum(stackX) + sum(stackY) + sum(stackR))
