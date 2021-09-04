X = list(map(int, input()))

def adjcent(a, b):
    if a == 9 and b == 0:
        return True
    if b - a == 1:
        return True
    return False

if X[0] == X[1] == X[2] == X[3]:
    print("Weak")
    exit()

if sum([adjcent(X[i], X[i+1]) for i in range(3)]) == 3:
    print("Weak")
else:
    print("Strong")