class Solution:
    def check(self, nums: List[int]) -> bool:
        leftMin = float('inf')
        points = []
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                points.append(i)
        if len(points)>1:
            return False
        if len(points)==0:
            return True
        idx = points[0]
        for i in range(0,idx):
            leftMin = min(leftMin,nums[i])
        for i in range(idx,len(nums)):
            if nums[i]>leftMin:
                return False
        return True

                
