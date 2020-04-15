import sys

n=int(input())
pointList=[]

for i in range(n):
    pointList.append(input())

t_bfr=0
x_bfr=0
y_bfr=0

for point in pointList:
    tmp = point.split()
    t_aft = int(tmp[0])
    x_aft = int(tmp[1])
    y_aft = int(tmp[2])

    t_len = t_aft-t_bfr
    x_len = abs(x_aft-x_bfr)
    y_len = abs(y_aft-y_bfr)

    if t_len < (x_len+y_len):
        print("No")
        sys.exit()
    elif (t_len - (x_len+y_len))%2  != 0:
        print("No")
        sys.exit()
    else:
        t_bfr=t_aft
        x_bfr=x_aft
        y_bfr=y_aft
print("Yes")
