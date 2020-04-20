n,m = [int(x) for x in input().split()]
aList =  [int(x) for x in input().split()]

sumA = sum(aList)
if n < sumA:
    print('-1')
else:
    print(n-sumA)
