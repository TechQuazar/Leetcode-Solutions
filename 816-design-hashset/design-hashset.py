class MyHashSet:

    def __init__(self):
        self.hash = 10**6 + 7
        self.arr = [False for _ in range(self.hash)]
        

    def add(self, key: int) -> None:
        self.arr[key%self.hash] = True

    def remove(self, key: int) -> None:
        if self.arr[key%self.hash]:
            self.arr[key%self.hash] = False

    def contains(self, key: int) -> bool:
        return self.arr[key%self.hash]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)