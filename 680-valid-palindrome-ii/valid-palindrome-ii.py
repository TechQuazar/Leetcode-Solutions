class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i=0
        j=n-1
        while i<j:
            if s[i]!=s[j]:
                l,r = i+1,j
                res = True
                while l<r:
                    if s[l]!=s[r]:
                        res = False
                        break
                    l+=1
                    r-=1
                if res:
                    return True
                res = True
                l,r = i,j-1
                while l<r:
                    if s[l]!=s[r]:
                        res = False
                        break
                    l+=1
                    r-=1
                return res
            else:
                i+=1
                j-=1

        return True