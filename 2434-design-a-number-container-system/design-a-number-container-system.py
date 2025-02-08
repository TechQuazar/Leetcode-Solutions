class NumberContainers:
    
    def __init__(self):
        self.indexToNumber = defaultdict(int)
        self.numberToIndex = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        # remove from number to index - Lazy update, perform removal in Find cause then its log(n)*k
        # self.numberToIndex[prevNumber].remove(index) # this is O(N), so dont perform it here
        # normal
        self.indexToNumber[index] = number
        # add to heap
        heapq.heappush(self.numberToIndex[number],index)


    def find(self, number: int) -> int:
        if len(self.numberToIndex[number])==0:
            return -1
        while len(self.numberToIndex[number])>0:
            index = self.numberToIndex[number][0] # first index in the list
            if self.indexToNumber[index] == number:
                return index
            # the index is stale, remove it
            heapq.heappop(self.numberToIndex[number])
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)