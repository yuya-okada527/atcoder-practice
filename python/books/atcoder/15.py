"""
PAST3回目 E

問題
1,2,3,…,N の番号がついた N 個の頂点と 1,2,3,…,M の番号がついた M 本の無向辺からなる無向グラフが与えられます。 辺 i は頂点 uiと viを双方向につないでいます。
それぞれの頂点には色を塗ることが可能で、はじめ頂点 i は色 ciで塗られています(この問題において、色は 1 以上 10**5以下の整数で表されます)。
それぞれの頂点にはスプリンクラーが設置されています。 頂点 i にあるスプリンクラーを起動すると、頂点 i に隣接する全ての頂点の色がスプリンクラー起動時点の頂点 i の色で塗り替えられます。

以下の形式で与えられる Q 個のクエリ s1,s2,…,sQを順番に処理してください。
- 頂点 x の現在の色を出力する。その後、頂点 x にあるスプリンクラーを起動する。1 x という形式で与えられる。
- 頂点 x の現在の色を出力する。その後、頂点 x の色を y で上書きする。2 x y という形式で与えられる。
"""

def f(graph, colors, queries):
    result = []
    for query in queries:
        if len(query) == 2:
            x = query[1] - 1
            color = colors[x]
            result.append(color)
            for y in graph[x]:
                colors[y] = color
        else:
            x = query[1] - 1
            result.append(colors[x])
            colors[x] = query[2]
    return result


def test():
    # cases = []
    #     "graph": [
    #         []
    #     ]
    # ]
    pass


def main():
    n, m, q = map(int, input().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        G[u].append(v)
        G[v].append(u)
    C = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(q)]
    for ans in f(G, C, Q):
        print(ans)

main()
