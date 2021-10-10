from collections import deque

S = input()
Q = int(input())
inv = False
s_deque = deque()
for s in S:
    s_deque.append(s)

for _ in range(Q):
    query = input()
    if query.startswith("1"):
        inv = not inv
    else:
        t, f, c = query.split()
        if inv:
            if f == "1":
                s_deque.append(c)
            else:
                s_deque.appendleft(c)
        else:
            if f == "1":
                s_deque.appendleft(c)
            else:
                s_deque.append(c)
ans = "".join(s_deque)
if inv:
    ans = ans[::-1]
print(ans)
