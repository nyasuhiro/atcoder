n,k = map(int,input().split())
modnk = n % k
if modnk < abs(modnk - k):
    print(modnk)
else:
    print(abs(modnk - k))
