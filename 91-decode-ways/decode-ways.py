class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {}
        def recur(i):
            if i==n:
                return 1
            total = 0
            if i in cache:
                return cache[i]
            if s[i]!='0':
                total+=recur(i+1)
            if i+1<n and (s[i]=='1' or s[i]=='2' and s[i+1]<='6'):
                total+= recur(i+2)
            cache[i] = total
            return total

        return recur(0)