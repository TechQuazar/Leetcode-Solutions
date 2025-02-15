class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        def solve(x):
            target = x*x
            num = str(target)
            arr = [ch for ch in num]
            n = len(arr)
            # print('X, target',x,target,arr)
            
            def recur(curr,prev,total):
                # print(curr,prev,total)
                if curr==n and total==x and curr==prev:
                    return True
                if curr>=n:
                    return False
                # take curr
                temp = ''
                for i in range(prev, curr+1):
                    temp+=arr[i]
                res = False
                res |= recur(curr+1,curr+1,total+int(temp))
                # leave curr
                res |= recur(curr+1,prev,total)
                return res

            res = recur(0,0,0)
            # print('Res',res)      
            return target if res else 0                 


        for i in range(1,n+1):
            res+= solve(i)
        return res