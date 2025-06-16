class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        TC O(N**2) SC O(N) call stack
        """
        wordSet = set(wordDict)
        n = len(s)
        @cache
        def recur(i):
            if i==n:
                return True
            for end in range(i+1,n+1):
                if s[i:end] in wordSet and recur(end):
                    return True
            return False
        return recur(0)