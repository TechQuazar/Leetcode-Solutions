class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # create dp
        m = len(str1)
        n = len(str2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(n+1):
            dp[0][i]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 
        lcs_len = dp[m][n]
        #find lcs string
        i = m
        j = n
        lcs = ""
        while(i>0 and j>0):
            if str1[i-1] == str2[j-1]:
                lcs+=str1[i-1]
                i-=1
                j-=1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i-=1
                else:
                    j-=1
        lcs = lcs[::-1]
        # find scs
        res=""
        i=0
        j=0
        k=0
        while k<lcs_len and i<m and j<n:
            if lcs[k] != str1[i] and lcs[k] != str2[j]:
                # res+= str1[i]+str2[j]
                # i+=1
                # j+=1 35/49 testcase pass
                while str1[i]!=lcs[k]:
                    res+=str1[i]
                    i+=1
                while str2[j]!=lcs[k]:
                    res+=str2[j]
                    j+=1
            else:
                if lcs[k] == str1[i]:
                    while str2[j] !=lcs[k]:
                        res+= str2[j]
                        j+=1
                else:
                    while str1[i] !=lcs[k]:
                        res+= str1[i]
                        i+=1
                res+=lcs[k]
                i+=1
                j+=1
                k+=1
        if i<m:
            while i<m:
                res+=str1[i]
                i+=1
            
        if j<n:
           while j<n:
                res+=str2[j]
                j+=1
        return res
