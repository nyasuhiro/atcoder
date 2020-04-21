import queue

K = int(input())
q = queue.Queue()
count=0

for i in range(1,10):
    q.put(i)
x=0
while True:
    count+=1
    x = q.get()

    if count==K:
        break

    xmod10 = x%10

    if xmod10 != 0 :
        q.put(10*x + xmod10 - 1)

    q.put(10*x + xmod10)

    if xmod10 != 9:
        q.put(10*x + xmod10 + 1)

print(x)
