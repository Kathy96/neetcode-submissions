class FreqStack:

    def __init__(self):
        self.counter = {}
        self.stack = {}
        self.maxCount = 0

    def push(self, val: int) -> None:
        curCnt = self.counter.get(val, 0) + 1
        self.counter[val] = curCnt
        if curCnt > self.maxCount:
            self.maxCount = curCnt
            self.stack[curCnt] = []
        self.stack[curCnt].append(val)

    def pop(self) -> int:
        maxVal = self.stack[self.maxCount].pop()
        self.counter[maxVal] -= 1
        if len(self.stack[self.maxCount]) == 0:
            del self.stack[self.maxCount]
            self.maxCount -= 1
        return maxVal
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()