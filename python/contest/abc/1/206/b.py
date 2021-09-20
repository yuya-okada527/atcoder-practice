n = int(input())
money = 0
for i in range(1, n):
    money += i
    if money >= n:
        print(i)
        exit()
print(1)