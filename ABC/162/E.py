# countBcd[i] : 最大公約数がiとなる数列の個数
# 全てiの倍数である数列の数はint(K/i) ** N ただし、全てi*2,i*3・・・の場合を除く

N, K = [int(x) for x in input().split()]
countBcd = [0]*(K+1)
mod=10**9+7
sumTotal=0
for i in range(K,0,-1):
    # modで除算しないととても遅い 
    countBcd[i] = pow(K//i,N,mod)

    for j in range(i*2,K+1,i):
        countBcd[i] -= countBcd[j]

    sumTotal += i*countBcd[i]%mod

print(sumTotal%mod)
