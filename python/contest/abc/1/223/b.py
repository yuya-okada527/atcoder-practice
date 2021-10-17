s = input()


def left(s):
    return s[1:] + s[0]

def right(s):
    return s[-1] + s[:-1]


temp = []
for _ in range(len(s) + 10):
    s = left(s)
    temp.append(s)

temp.sort()
print(temp[0])
print(temp[-1])
