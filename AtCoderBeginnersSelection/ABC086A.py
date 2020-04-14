ab = input().split()
a = int(ab[0])
b = int(ab[1])

ans = "Even" if a*b%2==0 else "Odd"
print(ans)
