class Solution:
    def triangularSum(self, nums: List[int]) -> int:
    
        while len(nums)>1:
            i = 0
            temp = []
            while i<len(nums)-1:
                temp.append((nums[i]+nums[i+1])%10)
                i+=1
            nums = temp
        return nums[0]
