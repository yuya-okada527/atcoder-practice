A, B, W = map(int, input().split())

w_g = 1000 * W
min_ans = 10 ** 15
max_ans = - 10 ** 15
for x in range(1, 10**6+10):
    if A * x <= w_g <= B * x:
        min_ans = min(min_ans, x)
        max_ans = max(max_ans, x)

if min_ans == 10 ** 15:
    print("UNSATISFIABLE")
else:
    print(min_ans, max_ans)
