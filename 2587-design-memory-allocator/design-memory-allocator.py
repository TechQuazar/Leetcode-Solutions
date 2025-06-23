class Allocator:

    def __init__(self, n: int):
        self.size = n
        self.arr = [0]*n
        self.map  = defaultdict(list)# mID to (start idx, size)

    def allocate(self, size: int, mID: int) -> int:
        l,r = 0,0
        if size>self.size:
            return -1

        def fill(l,r):
            for i in range(l,r+1):
                self.arr[i] = mID
            return
        
        free = 0
        while r<self.size:
            curr = self.arr[r]
            if curr==0:
                free+=1
                if size==free:
                    fill(l,r)
                    self.map[mID].append((l,size))
                    return l
            else:
                r+=1
                free = 0
                l = r
                continue
            r+=1
        return -1

    def freeMemory(self, mID: int) -> int:
        if mID not in self.map:
            return 0
        total = 0
        for idx,size in self.map[mID]:
            total+= size
            for i in range(idx, idx+size):
                self.arr[i]=0
        del self.map[mID]
        return total

    # [1 2 3 0 0 0 0 0 0 0]

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)