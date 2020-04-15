S=input()
T=""

dre="dreamerase"
dr="dreamer"
d="dream"
er="eraser"
e="erase"

while True:
    if S == T:
        print("YES")
        break
    elif S.startswith(T+dre):
        T = T+d
    elif S.startswith(T+dr):
        T = T+dr
    elif S.startswith(T+d):
        T = T+d
    elif S.startswith(T+er):
        T = T+er
    elif S.startswith(T+e):
        T = T+e
    else:
        print("NO")
        break
