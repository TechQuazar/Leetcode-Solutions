class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.idxMap = {}
        start = 1
        for i,x in enumerate(w):
            self.idxMap[(start,start+x-1)] = i
            start+=x

    def pickIndex(self) -> int:
        """
        we have to pick the index based on its probability
        essentially, we have to spread the weights such that when we pick one the probab remains correct
        so [1,3] => [a,x,x,x]
        at most 10**4 values in total
        so list of x = sum(w) values
        but each can be 10**5 max, so 10**9 total values of that list
        each value can be assigned to some block
        like between 1-100 to a, 101-400 to b. Then just print where the rand function lands
        OK
        1. total = sum(w)
        2. rand function must pick between 1 and total
        3. if it lands on x, check where it lands in the map
        4. map -> (low, high) -> idx
        """
        x = random.randint(1,self.total)
        for k,v in self.idxMap.items():
            low, high = k
            if low<=x<=high:
                return v


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()