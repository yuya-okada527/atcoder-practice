from collections import OrderedDict


class OrderedSet:

    def __init__(self):
        self.ordered_dict = OrderedDict()

    def __contains__(self, item):
        return item in self.ordered_dict

    def __len__(self):
        return len(self.ordered_dict)

    def __iter__(self):
        return iter(self.ordered_dict)

    def add(self, item):
        self.ordered_dict[item] = None

    def discard(self, item):
        if item in self:
            del self.ordered_dict[item]

    def first(self):
        if len(self) > 0:
            return next(iter(self))


n, q = map(int, input().split())
oset = OrderedSet()
i = 1
ans = []
for _ in range(q):
    event = input()
    if event.startswith("1"):
        oset.add(i)
        i += 1
    elif event.startswith("2"):
        _, x = map(int, event.split())
        oset.discard(x)
    else:
        ans.append(oset.first())
for a in ans:
    print(a)
