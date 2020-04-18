# bitDPで解く
# N桁のY/Nの状態をbitで表し、Sとする。
# YYYNNYY = "1110011"
# dp[S]は状態Sの時のコスト
# SのパターンはN桁のYorNなので2**n
# dpの初期値を設定上の最大値として、各商品リストを買った時に
# dp[S|s[i]] > dp[S] + cならばdp[S|s[i]]を更新する。


# 入力部分
n,m = [int(x) for x in input().split()]
sList=[]
cList=[]
for i in range(m):
    sc=input().split()
    sList.append(int(sc[0].replace("Y","1").replace("N","0"),2))
    cList.append(int(sc[1]))

inf = int(1000000000*1000)

# dpを初期化。初期値は最大値
totalPattern = 2**n
dp=[inf]*totalPattern

# dp[0]からスタート。dp[0]は何も買っていない状態(NNNNNNNN)なのでコスト0
# 全て買えた状態の時は全てのbitが1の時(YYYYYYYY) = dp[totalPattern-1]
dp[0]=0

# 商品数分ループする。
for i in range(m):
    # 各状態パターンで商品iを買った時を検証する。
    for nowStatus in range(totalPattern):
        # 商品iを買う = 現在の状態と商品iのORで新しい状態になる
        newStatus = nowStatus | sList[i]
        # 現在のコストに商品iのコストを足したコストを計算する
        newCost = dp[nowStatus] + cList[i]
        # もし現時点で設定されている新しい状態のコストよりも計算したコストが安ければ更新する。
        # つまり新しい状態を作るのによりよい買い方が見つかったということ
        if dp[newStatus] > newCost:
            dp[newStatus] = newCost

# もし最終形が一度も更新されない = 最終形に到達する組合せがないなら
# -1を出力
if dp[totalPattern-1] == inf:
    print("-1")
else:
    print(dp[totalPattern-1])
