class Solution:
    def reverse(self, x: int) -> int:
        low = -2**31
        high = 2**31 - 1
        curr = 0
        isNeg = True if x<0 else False
        if isNeg:
            x = -1*x
        while x>0:
            curr= curr*10 + x%10
            x = x//10
            if not (low<=curr<=high):
                return 0

        return curr if not isNeg else curr*-1