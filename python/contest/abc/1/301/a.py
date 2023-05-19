n = int(input())
s = input()
t = 0
a = 0
win_n = n//2 if n%2 == 0 else n//2+1
for i in s:
    if i == 'A':
        a += 1
    else:
        t += 1
    if win_n <= a or win_n <= t:
        break
if win_n == a:
    print("A")
else:
    print("T")
