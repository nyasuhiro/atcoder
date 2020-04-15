nq=input().split()
numUsers=int(nq[0])
logRow=int(nq[1])

logList=[]
for i in range(logRow):
    logList.append(input())

followList=[["N" for i in range(numUsers)] for j in range(numUsers)]

for logRow in logList:
    log = logRow.split()
    if log[0] == "1":
        a = int(log[1])-1
        b = int(log[2])-1
        followList[a][b] = "Y"
    elif log[0] == "2":
        a = int(log[1])-1
        for i in range(numUsers):
            if followList[i][a] == "Y":
                followList[a][i] = "Y"
    else:
        a = int(log[1])-1
        aList=[]
        for i in range(numUsers):
            if followList[a][i] == "Y":
                aList.append(i)
        for follower in aList:
            for j in range(numUsers):
                if (followList[follower][j] == "Y") and (j != a):
                    followList[a][j] ="Y"

for i in range(numUsers):
    print(*followList[i],sep='')
