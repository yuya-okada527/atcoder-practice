N = int(input())
ST = []
for _ in range(N):
    s, t = input().split()
    ST.append((s, int(t)))
sorted_st = sorted(ST, key=lambda x: x[1], reverse=True)

print(sorted_st[1][0])
