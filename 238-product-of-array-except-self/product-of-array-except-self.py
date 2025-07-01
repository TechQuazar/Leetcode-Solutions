class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1 2 3 4]
        left = [1 2 6 24]
        right =[24 24 12 4]
        """
        n = len(nums)
        left = []
        right = []
        for i in range(n):
            if not left:
                left.append(nums[i])
            else:
                left.append(left[-1]*nums[i])
        
        for i in range(n-1,-1,-1):
            if not right:
                right.append(nums[i])
            else:
                right.append(right[-1]*nums[i])
        right = right[::-1]
        res = [0]*n
        for i in range(1,n-1):
            res[i] = left[i-1]*right[i+1]
            
        res[0] = right[1]
        res[-1] = left[n-2]
        return res
