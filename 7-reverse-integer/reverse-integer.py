class Solution:
    def reverse(self, x: int) -> int:
        # low = -2**31, dont need to check this cause "The minimum 32-bit signed integer is -2147483648, but the maximum reversed positive number is 2147483647, which when negated becomes -2147483647 — still valid."
        high = 2**31 - 1
        curr = 0
        isNeg = True if x<0 else False
        if isNeg:
            x = -1*x
        while x>0:
            digit = x%10
            x = x//10
            if curr > high//10 or (curr==high//10 and digit>7):
                return 0
            curr = curr*10 + digit

        return curr if not isNeg else curr*-1