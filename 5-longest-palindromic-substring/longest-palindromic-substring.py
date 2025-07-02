class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        maxLen = 0
        for i in range(n):
            # odd len
            l,r = i,i
            while l-1>=0 and r+1<n and s[l-1]==s[r+1]:
                l-=1
                r+=1
            if r-l+1>maxLen:
                res = s[l:r+1]
                maxLen = r-l+1
            # even length
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if r-l+1>maxLen:
                res = s[l:r+1]
                maxLen = r-l+1
        
        return res