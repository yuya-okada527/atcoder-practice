"""
ABC81-C
問題
高橋君は，N 個のボールを持っています． 最初，i 番目のボールには，整数 Aiが書かれています．
高橋君は，いくつかのボールに書かれている整数を書き換えて，N 個のボールに書かれている整数が K 種類以下になるようにしたいです．
高橋君は，少なくとも何個のボールの整数を書き換える必要があるでしょうか？

制約
1 ≤ K ≤ N ≤ 200000
1 ≤ A
i ≤ N
与えられる数値はすべて整数


方針
1. N個の辞書で、整数の個数を管理する
2. 最初の整数数-K個だけ変える必要がある
3. 少ない順に変えていく
"""
from collections import Counter

n, k = map(int, input().split())
A = list(map(int, input().split()))
counter = Counter(A)

if len(counter) <= k:
    print(0)
    exit()


sorted_counter = sorted(counter.values())
ans = sum(sorted_counter[:len(counter)-k])

print(ans)
