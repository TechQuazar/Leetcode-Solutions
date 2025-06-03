class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            left_neighbor = nums[mid - 1] if mid > 0 else float('-inf')
            right_neighbor = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')
            
            # Check if mid is a peak
            if nums[mid] > left_neighbor and nums[mid] > right_neighbor:
                return mid
            
            # If right neighbor is greater, move right
            if nums[mid] < right_neighbor:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  # Just a fallback; shouldn't happen due to the problem guarantee
        