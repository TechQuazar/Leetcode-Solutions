class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0]=='0':
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = 1
        if n==1:
            return dp[0]
        dp[1] = dp[0] if s[1]!='0' else 0
        if 10<=int(s[:2])<=26:
            dp[1]+=1

        for i in range(2,n):
            total = 0
            if s[i]!='0':
                total+=dp[i-1]
            if  s[i-1]=='1' or (s[i-1]=='2' and int(s[i])<=6):
                total+=dp[i-2]
            dp[i] = total
        return dp[-1]