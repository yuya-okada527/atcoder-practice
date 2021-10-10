A, B, W = map(int, input().split())
w_gram = W * 1000
min_x = 10 ** 15
max_x = - 10 ** 15
for x in range(1, 10**6+100):
    if A * x <= w_gram <= B * x:
        max_x = max(max_x, x)
        min_x = min(min_x, x)

if min_x == 10 ** 15:
    print("UNSATISFIABLE")
else:
    print(min_x, max_x)
