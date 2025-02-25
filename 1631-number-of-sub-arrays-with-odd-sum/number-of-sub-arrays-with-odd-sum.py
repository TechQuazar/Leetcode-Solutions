class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # hints are useful

        oddCount = 0
        evenCount = 0
        currSum = 0
        res = 0
        n = len(arr)
        MOD = 10**9 + 7
        for i in range(n):
            currSum+=arr[i]
            currSum%=2
            if currSum==0: # even
                evenCount+=1
                res+= oddCount
                res%=MOD
            else:
                oddCount+=1
                res+= 1 + evenCount
                res%=MOD

        return res%MOD

        

        