from re import M
from typing import Dict, List

GRAPH = {
    "A": {
        "B": 10,
        "C": 20,
        "D": 12,
        "E": 15
    },
    "B": {
        "A": 10,
        "E": 10
    },
    "C": {
        "A": 20,
        "D": 10,
        "F": 25,
        "G": 20,
        "H": 30
    },
    "D": {
        "A": 12,
        "C": 10,
        "E": 15,
        "H": 20
    },
    "E": {
        "A": 15,
        "B": 10,
        "D": 15,
        "H": 15,
        "I": 18
    },
    "F": {
        "C": 25,
        "G": 5
    },
    "G": {
        "C": 20,
        "F": 5,
        "H": 35
    },
    "H": {
        "C": 30,
        "D": 20,
        "E": 15,
        "G": 35,
        "I": 12
    },
    "I": {
        "E": 18,
        "H": 12
    }
}

def search_route(current: str, before_route: List[str], routes: List[List[str]], graph: Dict[str, Dict[str, int]] = GRAPH) -> None:
    """経路を探索する

    Args:
        current (str): 現在地 例: "A"
        before_route (List[str]): これまでの経路 例: ["A", "C"]
        routes (List[List[str]]): これまで探索完了した経路のリスト 例: [["A", "C", "A"], ["A", "C", "D", "A"]]
        graph (Dict[str, Dict[str, int]], optional): 通過可能経路のグラフ 例: {"A": {"C": 10}} <- AからCへコスト10で行けるという意味. Defaults to GRAPH.
    """
    for next in graph[current].keys():
        # TODO やっぱりここの判定甘い気がする
        if next in before_route:
            # 2回目通る場合は、全経路リストに追加
            routes.append(before_route + [next])
        else:
            # 初めて通る場合は、経路に追加した上で、さらに探索する
            search_route(next, before_route + [next], routes, graph)


def filter_routes(routes: List[str], graph: Dict[str, Dict[str, int]] = GRAPH) -> List[str]:
    result = []
    for route in routes:
        # 「始点と終点が同じ」かつ「全地点を経由している」
        if route[0] == route[-1] and len(set(route)) == len(graph):
            result.append(route)
    return result


def calc_cost(route: List[str], graph:  Dict[str, Dict[str, int]] = GRAPH) -> int:
    result = 0
    for i in range(len(route)-1):
        result += graph[route[i]][route[i+1]]
    return result


# 全スタート位置からのコストと経路のリスト
all_cost_and_route = []
for start in GRAPH.keys():
    # スタート位置固定の経路を列挙
    routes = []
    search_route(start, [start], routes, GRAPH)

    # 条件を満たしている経路のみに絞る
    valid_routes = filter_routes(routes)

    # 経路のコストを全部計算する
    for route in valid_routes:
        cost = calc_cost(route, GRAPH)
        all_cost_and_route.append((cost, route))

sorted_routes = sorted(all_cost_and_route)

print(sorted_routes[0])



# before_route = ["A"]
# routes = []
# search_route("A", before_route, routes)

# for route in routes:
#     print(route)



def test_search_route():
    routes = []
    search_route("A", ["A"], routes, {
        "A": {
            "C": 20,
            "D": 12,
            "E": 15
        },
        "C": {
            "A": 20,
            "D": 10
        },
        "D": {
            "A": 12,
            "C": 10,
            "E": 15
        },
        "E": {
            "A": 15,
            "D": 15
        }
    })
    for route in routes:
        assert max([route.count(node) for node in GRAPH.keys()]) == 2
        assert [route.count(node) for node in GRAPH.keys()].count(2) == 1
    print("Pass: 1つの経路に同じ場所は最大2回しか出てこない")
    print("Pass: 1つの経路に同じ場所が2回出てくるのは1度のみ")

    actual_routes = set(["_".join(route) for route in routes])
    expected_routes = set(
        [
            "_".join(route) for route in [
                ['A', 'C', 'A'],
                ['A', 'C', 'D', 'A'],
                ['A', 'C', 'D', 'C'],
                ['A', 'C', 'D', 'E', 'A'],
                ['A', 'C', 'D', 'E', 'D'],
                ['A', 'D', 'A'],
                ['A', 'D', 'C', 'A'],
                ['A', 'D', 'C', 'D'],
                ['A', 'D', 'E', 'A'],
                ['A', 'D', 'E', 'D'],
                ['A', 'E', 'A'],
                ['A', 'E', 'D', 'A'],
                ['A', 'E', 'D', 'C', 'A'],
                ['A', 'E', 'D', 'C', 'D'],
                ['A', 'E', 'D', 'E']
            ]
        ]
    )
    assert actual_routes == expected_routes

    print("Pass: 想定する経路の組み合わせになること")

test_search_route()

def test_filter_routes():
    routes = [
        ['A', 'C', 'A'],
        ['A', 'C', 'D', 'A'],
        ['A', 'C', 'D', 'C'],
        ['A', 'C', 'D', 'E', 'A'],
        ['A', 'C', 'D', 'E', 'D'],
        ['A', 'D', 'A'],
        ['A', 'D', 'C', 'A'],
        ['A', 'D', 'C', 'D'],
        ['A', 'D', 'E', 'A'],
        ['A', 'D', 'E', 'D'],
        ['A', 'E', 'A'],
        ['A', 'E', 'D', 'A'],
        ['A', 'E', 'D', 'C', 'A'],
        ['A', 'E', 'D', 'C', 'D'],
        ['A', 'E', 'D', 'E']
    ]
    graph = {
        "A": {
            "C": 20,
            "D": 12,
            "E": 15
        },
        "C": {
            "A": 20,
            "D": 10
        },
        "D": {
            "A": 12,
            "C": 10,
            "E": 15
        },
        "E": {
            "A": 15,
            "D": 15
        }
    }
    actual_routes = set(
        ["_".join(route) for route in filter_routes(routes, graph)]
    )
    expected_routes = set(
        ["_".join(route) for route in [
            ['A', 'C', 'D', 'E', 'A'],
            ['A', 'E', 'D', 'C', 'A']
        ]]
    )
    assert actual_routes == expected_routes
    print("Pass: 想定する経路に絞れていること")

test_filter_routes()


def test_calc_cost():
    graph = {
        "A": {
            "C": 20,
            "D": 12,
            "E": 15
        },
        "C": {
            "A": 20,
            "D": 10
        },
        "D": {
            "A": 12,
            "C": 10,
            "E": 15
        },
        "E": {
            "A": 15,
            "D": 15
        }
    }
    assert calc_cost(["A", "C", "A"], graph) == 40
    assert calc_cost(["A", "C", "D", "E", "A"]) == 60
    print("Pass: コスト計算OK")

test_calc_cost()
