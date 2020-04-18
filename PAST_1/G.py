N=int(input())
A=[[0 for x in range(N)] for y in range(N)]
for i in range(N-1):
    tmp = [int(x) for x in input().split()]
    for j in range(i+1,N):
        A[i][j] = tmp[j-(i+1)]

# 3グループに分ける→各人に0,1,2のラベルをつける総組合せ
# 3で割った余りをそれぞれに設定する
# 3進数の各ビットの値がグループ番号に相当する
# 総計算数は3**N
# 例：N=10の時
# 0:0000000000 → 全員グループ0
# 1:0000000001 → 1番目の人だけグループ1,それ以外はグループ0
# 2:0000000002 → 1番目の人だけグループ2,それ以外はグループ0
# 3:0000000010 → 2番目の人だけグループ1,それ以外はグループ0
# 4:0000000011 → 1,2番目の人だけグループ1,それ以外はグループ0
# 5:0000000012 → 1番目の人がグループ2,2番目の人がグループ1,それ以外はグループ0
# 6:0000000020 → 2番目の人だけグループ2,それ以外はグループ0
# のように続く

totalLoop=3**N
maxVal=-1000000*N
for i in range(totalLoop):
    bitGroup=[]
    shiftI=i
    tmpMax=0
    for j in range(N):
        bitGroup.append(int(shiftI%3))
        shiftI=int(shiftI/3)
    for k in range(N):
        for l in range(k+1,N):
            if bitGroup[k] == bitGroup[l]:
                tmpMax+=A[k][l]
    if tmpMax > maxVal:
        maxVal = tmpMax

print(maxVal)
