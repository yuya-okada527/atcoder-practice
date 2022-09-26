s = input()
# print(s)
if not s.startswith("A"):
    # print("starts")
    print("WA")
    exit()
if not s[2:-1].count("C") == 1:
    # print("not C")
    print("WA")
    exit()
s = s[1:]
# print(s)
idx = s[1:-1].index("C")
s = s[:idx+1] + s[idx+2:]
# print(s)
if s == s.lower():
    print("AC")
    exit()
print("WA")
