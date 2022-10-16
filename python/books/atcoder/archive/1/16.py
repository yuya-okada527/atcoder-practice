"""
abc122 C

問題
A, C, G, T からなる長さ N の文字列 S が与えられます。以下の Q 個の問いに答えてください。

- 問 i (1≤i≤Q): 整数 li,ri(1≤li<ri≤N) が与えられる。S の先頭から li文字目から ri文字目までの (両端含む) 部分文字列を考える。この文字列に AC は部分文字列として何回現れるか。
"""
n, q = map(int, input().split())
s = input()
cs = [0] * (n+1)
for i in range(1, n):
    cs[i+1] = cs[i] + (s[i-1:i+1] == "AC")
for _ in range(q):
    l, r = map(int, input().split())
    print(cs[r] - cs[l])
