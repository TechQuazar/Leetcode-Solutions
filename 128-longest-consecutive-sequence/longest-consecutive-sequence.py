class Solution:
    def longestConsecutive(self, nums):
        seen = set(nums)
        res = 0
        for num in seen: # if you do for num in nums you get TLE.
            if num-1 not in seen:
                curr = num
                count = 0
                while curr in seen:
                    count+=1
                    curr +=1
                res = max(res,count)

        return res
