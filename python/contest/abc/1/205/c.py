A, B, C = map(int, input().split())
c_is_even = C % 2 == 0
if c_is_even:
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")
    exit()
