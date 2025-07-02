class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def recur(i,path):
            res.append(list(path))
            if i>=n:
                return

            for j in range(i,n):
                path.append(nums[j])
                recur(j+1,path)
                path.pop()
            return
        
        recur(0,[])
        return res