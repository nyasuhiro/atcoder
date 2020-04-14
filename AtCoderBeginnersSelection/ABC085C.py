import sys
ny=[int(x) for x in input().split()]

n=ny[0]
y=ny[1]

for i in range(n+1):
	for j in range(n-i+1):
		k=n-i-j
		tmp = y - 10000*i - 5000*j - 1000*k
		if tmp == 0:
			print(i,j,k)
			sys.exit()
		elif tmp < 0:
			break
		else:
			continue
print(-1,-1,-1)
