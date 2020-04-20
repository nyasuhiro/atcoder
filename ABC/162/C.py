# bcd[a][b] : aとbの最大公約数の値
K = int(input())
bcd=[[int(-1) for x in range(K+1)]for j in range(K+1)]


def retBcd(a,b):
    if bcd[a][b] != -1 :
        return bcd[a][b]
    if b == 0:
        bcd[a][b] = a
        bcd[b][a] = a
        return a
    else:
        ret = retBcd(b,a%b)
        bcd[a][b] = ret
        bcd[b][a] = ret
        return ret

sumTotal=0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            sumTotal += retBcd(retBcd(i,j),k)
print(sumTotal)
