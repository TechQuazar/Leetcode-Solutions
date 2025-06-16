class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        @cache
        def recur(s):
            if s=="":
                return True
            n = len(s)
            res = False
            curr = ""
            for i in range(n):
                curr+=s[i]
                if curr in wordSet:
                    res = res or recur(s[i+1:])
                    if res:
                        return True
            return res
        
        return recur(s)
        