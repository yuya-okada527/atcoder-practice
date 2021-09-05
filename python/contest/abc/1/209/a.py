A, B = map(int, input().split())

diff = B - A + 1
if diff < 0:
    print(0)
else:
    print(diff)