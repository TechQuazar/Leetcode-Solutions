class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        n = len(arr)
        res = []
        def backtrack(i,total, path):
            if i>=n or total>target:
                return
            if total==target:
                res.append(list(path))
                return
            if arr[i]+total<=target:
                path.append(arr[i])
                backtrack(i, total+arr[i],path)
                path.remove(arr[i])
            
            backtrack(i+1, total, path)
            return


        backtrack(0,0,[])
        return res
