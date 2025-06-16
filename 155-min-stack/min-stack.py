class MinStack:

    def __init__(self):
        self.st = []
        self.min = []
        self.currIdx = -1


    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(self.min[self.currIdx],val))
        self.currIdx+=1
        # print('self.min',self.min)

    def pop(self) -> None:
        del self.st[self.currIdx]
        del self.min[self.currIdx]
        self.currIdx-=1

    def top(self) -> int:
        return self.st[self.currIdx]
        

    def getMin(self) -> int:
        return self.min[self.currIdx]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()