class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        repeated work
        5 1 6
        brute force o(2**n)
        '''
        total = 0
        n = len(nums)
        def recur(i, curr):
            if i>=n:
                return curr
            return recur(i+1,curr^nums[i]) + recur(i+1,curr)
        return recur(0,0)

        