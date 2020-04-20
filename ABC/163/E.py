# スコアが高い順に右端 or 左端に置く事を考える
# dp[i][l] : l番目まで左に子がいる状態でi番目の子を動かす時の最大値
# python3.8.2ではTLE,pypy3 7.3.0 でACだった

n = int(input())
tmp = [int(x) for x in input().split()]

aList=[]
for i in range(n):
    aList.append([tmp[i],i])

aList.sort(reverse=True)

dp=[[int(-1) for i in range(n+1)] for j in range(n+1)]
dp[0][0] = 0

# スコアが高い順にi人動かす
for i in range(n):
    # 左側に置いた人数。i番目のループでは0〜i人まで左端に置く可能性がある
    for l in range(i+1):
        activity = aList[i][0]
        pos = aList[i][1]

        # 右端の今のポジション
        # totalで置いた数-左側に置いた数(i-l)を計算し、右端(n-1)から引く
        r = n-1-(i-l)

        # 左に置いた場合
        dp[i+1][l+1] = max(dp[i+1][l+1],dp[i][l] + abs(l-pos) * activity)

        # 右に置いた場合
        dp[i+1][l]   = max(dp[i+1][l],dp[i][l] + abs(r-pos) * activity)

print(max(dp[n]))
