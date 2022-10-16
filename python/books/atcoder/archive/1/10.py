import sys
import pprint

def xy(h, w):
    for y in range(h):
        for x in range(w):
            yield x, y


def is_blank(s, x, y):
    return s[y][x] == "."


def test_is_blank():
    s = [
        "..#",
        "#.#",
        "..."
    ]
    assert is_blank(s, 0, 0) == True
    assert is_blank(s, 1, 0) == True
    assert is_blank(s, 2, 0) == False
    assert is_blank(s, 0, 1) == False
    print("Passed: test_is_blank")


DIRECTIONS = [
    (-1, -1), # 左上
    (0, -1),  # 上
    (1, -1),  # 右上
    (-1, 0),  # 左
    (1, 0),   # 右
    (-1, 1),  # 左下
    (0, 1),   # 下
    (1, 1)    # 右下
]

def count_bomb(s, x, y):
    result = 0
    for _x, _y in DIRECTIONS:
        moved_x = x + _x
        moved_y = y + _y
        if moved_x < 0: continue            # 左
        elif moved_x >= len(s[0]): continue # 右
        elif moved_y < 0: continue          # 上
        elif moved_y >= len(s): continue    # 下
        else:                               # マップ上
            # 爆弾あり
            if not is_blank(s, moved_x, moved_y):
                result += 1
    return result


def search_bomb(s, x, y):
    if not is_blank(s, x, y):
        return "#"
    else:
        return str(count_bomb(s, x, y))


def test_search_bomb():
    s = [
        "..#",
        "#.#",
        "..."
    ]
    assert search_bomb(s, 0, 0) == "1"
    assert search_bomb(s, 1, 0) == "3"
    assert search_bomb(s, 2, 0) == "#"
    assert search_bomb(s, 0, 1) == "#"
    assert search_bomb(s, 1, 1) == "3"
    assert search_bomb(s, 2, 1) == "#"
    assert search_bomb(s, 0, 2) == "1"
    assert search_bomb(s, 1, 2) == "2"
    assert search_bomb(s, 2, 2) == "1"
    print("Passed: test_search_bomb")



def main():
    h, w = map(int, input().split())
    S = [input() for _ in range(h)]
    result = [["" for _ in range(w)] for _ in range(h)]
    for x, y in xy(h, w):
        result[y][x] = search_bomb(S, x, y)
    for r in result:
        print("".join(r))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_is_blank()
        test_search_bomb()
    else:
        main()
