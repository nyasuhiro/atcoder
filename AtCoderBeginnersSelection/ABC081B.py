N=input()
list=[int(x) for x in input().split()]

count=0
flg=True

while flg:
	for i, num in enumerate(list):	
		if num%2 != 0:
			flg=False
			break
		else:
			list[i] = num/2
	if flg:
		count+=1
print(count)
