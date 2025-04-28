class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''

        '''
        n = len(nums)
        totalProduct = 1
        l = 0
        res = 0
        for r in range(n):
            curr = nums[r]
            totalProduct*=curr
            while totalProduct>=k and l<=r:
                # print('tot,l,r',totalProduct,l,r)
                res+= (r-l)
                totalProduct//=nums[l]
                l+=1
        # print('total,l,r', totalProduct,l,r)
        res+= (r-l+1)*(r-l+2)//2
        return res