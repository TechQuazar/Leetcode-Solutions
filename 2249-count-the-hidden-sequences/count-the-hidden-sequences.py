class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        '''
        return number not generate
        if n = len(diff)
        seq = n+1
        
        BFE - [- - - - -] fix one, try rest. 
        [1 -3 4] l=1, u =6
        [x1 x2 x3 x4]
        x2-x1 = 1
        x3-x2 = -3
        x4-x3 = 4
        diff
        max = 4
        min = -3
        --
        OPT
        [x x+1 x-2 x+2]

        '''

        n = len(differences)
        possibleMin=0
        possibleMax=0
        curr = 0
        for i in range(n):
            curr += differences[i]
            possibleMin = min(possibleMin, curr)
            possibleMax = max(possibleMax, curr)
        # x+possibleMin >=lower
        # x+possibleMax <=upper
        res = max(0, (upper-lower) - (possibleMax - possibleMin)+1)
        
        return res
