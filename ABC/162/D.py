# Si, Sj, Skは必ずR,G,Bのどれか
# Rから1つ、Gから1つ、Bから1つ選ぶ組合せ
# Rの数 * Gの数 * Bの数 = 組合せの総数
# j-i != k-jは全体からj-i == k-jを引く
# i,jが決まるとkは2j-iと決まる

n = int(input())
S = input()

countR = S.count('R')
countG = S.count('G')
countB = S.count('B')

# R,G,Bの組み合わせ
total = countR * countG * countB

count=0
for i in range(n):
    for j in range(i+1,n):
        k = int(2*j - i)
        if k >= n:
            break
        if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            count+=1

total -= count

print(total)
