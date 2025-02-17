class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        cache = {}
        def recur(i,pro):
            nonlocal res
            if i==n:
                return
            if (i,pro) in cache:
                return
            # take curr
            currPro = pro*nums[i]
            res = max(res,currPro)
            recur(i+1,currPro)
            # start from curr
            res = max(res,nums[i])
            recur(i+1,nums[i])
            # leave curr
            recur(i+1,1)
            cache[(i,pro)] = True
            return

        recur(0,1)
        return res

