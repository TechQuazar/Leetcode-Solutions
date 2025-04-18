class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        BruteForce - write countAndSay (O(k))
        countAndSay(n) = RLE (CAS(n-1)), where CAS(1) = "1"
        CAS(n) = RLE(RLE(CAS(n-2)))
        O(n*k)
        '''
        curr = "1"
        for _ in range(2,n+1):
            res = ""
            i=0
            while i<len(curr):
                ch = curr[i]
                count = 1
                while i<len(curr)-1 and curr[i+1]==ch:
                    count+=1
                    i+=1
                res+= str(count)+ch
                i+=1
            curr=res

        return curr
                
            

