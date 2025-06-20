class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isUnique(s):
            return len(set(s))==len(s)

        def backtrack(idx, path):
            nonlocal maxLen
            if len(path)>maxLen:
                maxLen = len(path)
            for i in range(idx,len(arr)):
                combined = path + arr[i]
                if isUnique(combined):
                    backtrack(i+1,combined)
        
        maxLen = 0
        backtrack(0,"")
        return maxLen