class RandomizedSet:
    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)

        print(self.numList)
        print(self.numMap)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            index = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[index] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = index
            del self.numMap[val]

        print(self.numList)
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)


_set = RandomizedSet()
_set.insert(1)
_set.insert(2)
_set.remove(1)
