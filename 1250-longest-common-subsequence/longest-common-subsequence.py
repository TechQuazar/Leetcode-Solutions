class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        cache = {}
        def recur(i,j):
            if i>=m or j>=n:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            res = 0
            if text1[i]==text2[j]:
                res = 1+recur(i+1,j+1)
            else:
                res = max(recur(i+1,j),recur(i,j+1))
            cache[(i,j)] = res
            return res
        return recur(0,0)
            