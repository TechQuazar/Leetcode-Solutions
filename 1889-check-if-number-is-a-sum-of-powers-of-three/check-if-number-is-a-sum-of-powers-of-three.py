class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        '''
        n = 3^a + 3^b + ... + 1/0
        3, 9, 27, 81, 243, 729, 
        even powers of 3 except 1 form even
        odd powers of 3 except 1 form odd
        1. find the power x that makes 3^x > n
        2. Start from 3^x-1
        3. for each prev power, check if curr+3^i>n:
            if yes, skip that power i
            if no, continue
        4. Keep track of curr and check when curr==n
        '''
        power = []
        i=0
        while 3**i<=n:
            power.append(3**i)
            i+=1
        x = len(power)-1
        if x<0:
            return False
        
        cache = {}
        def recur(i,curr):
            if curr==n:
                return True
            if i<0:
                return False
            if (i,curr) in cache:
                return cache[(i,curr)]
            res = False
            if curr+power[i]>n:
                res |= recur(i-1,curr)
            else:
                res |= recur(i-1,curr+power[i])
            cache[(i,curr)] = res
            return res
        
        return recur(x,0)
        