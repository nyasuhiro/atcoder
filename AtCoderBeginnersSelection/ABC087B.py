a = int(input())
b = int(input())
c = int(input())
x = int(input())

count=0

for i in range(a+1):
	minus500 = x - 500*i
	if minus500 == 0:
		count+=1
		break
	elif minus500 < 0:
		break
	else:
		for j in range(b+1):
			minus100 = minus500 - 100*j
			if minus100 == 0:
				count+=1
				break
			elif minus100 < 0:
				break
			else:
				for k in range(c+1):
					minus50 = minus100 - 50*k
					if minus50 == 0:
						count+=1
						break
					elif minus50 < 0:
						break
					else:
						continue
print(count)
