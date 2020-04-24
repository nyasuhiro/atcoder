N,X,Y = map(int,input().split())

lenList = [0 for x in range(N)]
for start in range(1,N):
    for end in range(start+1,N+1):
        len = end - start
        if start <= X:
            if end <= X:
                lenList[len] += 1
            elif end < Y:
                len = min(len,((X-start) + 1 + (Y-end)))
                lenList[len] += 1
            else:
                len = (X-start) + 1 + (end-Y)
                lenList[len] += 1
        elif start < Y:
            if end < Y:
                len = min(len,(start-X) + 1 + (Y-end))
                lenList[len] += 1
            else:
                len = min(len,(start-X) + 1 + (end-Y))
                lenList[len] += 1
        else:
            lenList[len] += 1

for k in range(1,N):
    print(lenList[k])
