n = int(input())
A = list(map(int, input().split()))
combination = (n-1) * n // 2
print(combination)
print(len(set(A)))
print(combination - (n - len(set(A))))