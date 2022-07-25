class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.maximumDifference = 0
        x = max(self.__elements)
        for i in self.__elements:
            if i == x:
                continue
            else:
                res = x - i
                if res > self.maximumDifference:
                    self.maximumDifference = res
                else:
                    continue

        return self.maximumDifference

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)