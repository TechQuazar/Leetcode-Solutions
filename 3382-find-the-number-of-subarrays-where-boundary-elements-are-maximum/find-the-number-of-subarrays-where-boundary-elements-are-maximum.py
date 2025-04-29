class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     maxVal = nums[i]
        #     for j in range(i,n):
        #         maxVal = max(maxVal, nums[j])
        #         if nums[i]==nums[j] and nums[i]==maxVal:
        #             res+=1

        '''
        -- opt - mono decreasing stack. For each element, we need to keep a track of largest to
        its left. We pop from stack when curr is > top of stack to maintain mono decr
        essentially if 2 elements are same and there are some elements bw them that deletes them
        [1 4 3 2 3 2]
                 ^ st = [(4,1),(3,1),(2,1)] 3 =>[(4,1),(3,1)] 3. increase count of top => [(4,1),(3,2)]
        '''
        st = []
        res = 0
        for num in nums:
            while st and st[-1][0]<num:
                st.pop()
            if not st or st[-1][0]>num:
                st.append([num,0])
            st[-1][1]+=1
            res+=st[-1][1]
        return res