class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key].append((value,timestamp))
        else:
            i = len(self.dict[key])-1
            while i>=0:
                topVal, topTime = self.dict[key][i]
                if timestamp>=topTime:
                    break
                i-=1
            self.dict[key].insert(i+1,(value,timestamp))
        # print('dict',self.dict)
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.dict[key]:
            return ""
        i = len(self.dict[key])-1
        while i>=0:
            topVal, topTime = self.dict[key][i]
            if topTime<=timestamp:
                return topVal
            i-=1
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)