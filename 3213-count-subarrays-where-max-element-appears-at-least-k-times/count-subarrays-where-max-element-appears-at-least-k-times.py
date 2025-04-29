class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        
        '''
        st = []
        n = len(nums)
        maxNum = max(nums)
        res = 0
        for r in range(n):
            curr = nums[r]
            if curr==maxNum:
                st.append(r)
                if len(st)>k:
                    st.pop(0)

            if len(st)==k:
                left = st[0]
                res+= left+1
        return res