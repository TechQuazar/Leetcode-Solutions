class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.og = list(nums)

    def reset(self) -> List[int]:
        self.arr = list(self.og)
        return self.arr
        

    def shuffle(self) -> List[int]:
        n = len(self.arr)
        for i in range(n):
            swapIdx = random.randrange(i,n)
            self.arr[i],self.arr[swapIdx] = self.arr[swapIdx],self.arr[i]
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()