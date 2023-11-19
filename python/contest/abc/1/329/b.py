from typing import List
import unittest


def f(lst: List[int]):
    assert isinstance(lst, list)
    assert len(lst) != 0
    return sorted(set(lst))[-2]


def main():
    n = int(input())
    lst = map(int, input().split())
    ans = f(lst)
    print(ans)


class UnitTest(unittest.TestCase):
    def test_リスト以外(self):
        not_list_args = [None, "string", 1, True, {}]
        for args in not_list_args:
            with self.assertRaises(AssertionError):
                f(args)

    def test_空配列の場合(self):
        with self.assertRaises(AssertionError):
            f([])

    def test_ソート済み(self):
        self.assertEqual(f([1, 2, 3]), 2)

    def test_has_equal_num(self):
        self.assertEqual(f([1, 2, 2]), 1)


if __name__ == "__main__":
    unittest.main()
    # main()
