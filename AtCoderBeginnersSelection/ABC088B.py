n = input()
a = [int(x) for x in input().split()]
a.sort(reverse=True)
print(sum(a[0::2]) - sum(a[1::2]))
