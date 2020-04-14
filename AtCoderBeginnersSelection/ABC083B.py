nab=input().split()
n = int(nab[0])
a = int(nab[1])
b = int(nab[2])

total=0
for i in range(n+1):
	iList=[int(x) for x in list(str(i))]
	iSum=sum(iList)
	if iSum >= a and iSum <= b:
		total+=i
print(total)
