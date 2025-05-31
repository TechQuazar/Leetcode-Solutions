class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0 or (n>0 and s[0]=='0'):
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1,n):
            # i-1 + curr if valid
            # i-2 + (i-1,i) if valid
            indv, comb = 0,0
            if int(s[i])!=0:
                indv = dp[i-1]
            if s[i-1]!='0' and int(s[i-1]+s[i])<=26:
                comb = dp[i-2] if i-2>=0 else 1
            dp[i] = indv+comb
        
        return dp[-1]