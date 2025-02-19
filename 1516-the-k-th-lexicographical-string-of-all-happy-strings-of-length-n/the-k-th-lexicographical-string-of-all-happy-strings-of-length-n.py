class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        total = 3 if n==1 else 3*2**(n-1)
        if k>total:
            return ""
        # total//3 gives division, which can be used to select the first letter
        total_each = total//3
        div = (k-1)//total_each # start from 0
        rem = (k-1)%total_each # start from 0
        # print('total_each,div,rem',total_each,div,rem)
        # find val at div + rem idx in lex sorted arr
        res = ""
        count=-1

        def recur(st):
            nonlocal count, res

            if len(st)==n:
                count+=1
                if count==rem:
                    res=st
                    return True
                return False
            
            for ch in ["a","b","c"]:
                if ch == st[-1]:
                    continue
                if recur(st+ch):
                    return True
            return False

        start = ""
        if div==0:
            start='a'
        elif div==1:
            start='b'
        else:
            start='c'

        recur(start)
        return res
            

        