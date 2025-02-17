class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        seen = set(wordDict)
        cache = {}
        def recur(l,r):
            if r-l+1==0:
                return True
            if (l,r) in cache:
                return cache[(l,r)]
            res = False
            temp = ''
            for i in range(l,r+1):
                temp+= s[i]
                if temp in seen:
                    res |= recur(i+1,r)

            cache[(l,r)] = res
            return cache[(l,r)]

        return recur(0,n-1)
