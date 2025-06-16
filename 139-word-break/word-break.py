class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        DP botton up
        """
        wordSet = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True # Empty string is always "breakable"
        for i in range(1,n+1):
            for j in range(i):
                if s[j:i] in wordSet and dp[j]:
                    dp[i] = True
                    break
        return dp[n]