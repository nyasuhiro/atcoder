# 各ポイントから右回り(right)、左回り(left)の２通りで距離を計算する

K,N = map(int,input().split())
aList = [int(x) for x in input().split()]

minDist=pow(10,6)

for i in range(N-1):
    right=0
    left=0
    if i == 0:
        right = aList[N-1] - aList[0]
        left  = K - aList[1] + aList[0]
    elif i == N-1:
        right = K + aList[N-2] - aList[N-1]
        left  = aList[N-1] - a[0]
    else:
        right = K + aList[i-1] - aList[i]
        left  = K - aList[i+1] + aList[i]
    minDist =min(minDist,min(right,left))

print(minDist)
