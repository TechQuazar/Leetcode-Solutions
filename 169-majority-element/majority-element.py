class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        reset = True
        for i,num in enumerate(nums):
            if i==0 or reset:
                res = num
                count+=1
                reset = False
                continue
            if num!=res:
                count-=1
            else:
                count+=1
            
            if count<=0:
                reset = True

        return res