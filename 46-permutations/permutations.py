class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        def backtrack(path, used):
            if len(path)==n:
                res.append(list(path))
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i]=False
            return

        used = [False]*n
        backtrack([], used)
        return res