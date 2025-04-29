class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        BFE - move across in O(N) then update for window in O(K) -> O(N*K) time solution
        Can we get a O(n) or similar solution?
        repeated work - each time the window moves, you take out the L and add the R
        need some tool that will help us keep track of the max indices in the window and if
        the L has crossed it or some
        [1,3,-1,-3,5,3,6,7]
        
        [6]
        """
        st = [] # mono decr st
        n = len(nums)
        res = []
        for i in range(n):
            curr = nums[i]
            while st and st[-1][0]<curr:
                st.pop()
            if not st or st[-1][0]>=curr:
                st.append([curr,i])
            if i>=k-1:
                res.append(st[0][0])
                if i-(k-1)>= st[0][1]:
                    st.pop(0)
        return res



            