n, q = map(int, input().split())
lst = set()
i = 1
ans = []
for _ in range(q):
    event = input()
    if event.startswith("1"):
        lst.add(i)
        i += 1
    elif event.startswith("2"):
        _, x = map(int, event.split())
        lst.remove(x)
        # index = bisect_left(lst, x)
        # after = lst[index+1:]
        # lst = lst[:index]
        # lst.extend(after)
    else:
        ans.append(sorted(list(lst))[0])
for a in ans:
    print(a)
