class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        score -> len(arr)*sum(arr)
        BFE - generate subarray and find count -> O(n**3)
        prefix sum opt -> O(n**2)
        - is there repeated work?
        - 
        [a,b,c,d..,n] -> n*(n+1)//2
        2 1 4 3 5
        --^
        l r => 2 => 3
        shift l+1, update the score,
        if score<k, r+=1
        should be doable
        '''
        n = len(nums)
        l,r=0,0
        res = 0
        score = 0
        totalSum = 0
        while r<n:
            curr = nums[r]
            totalSum+=curr
            score = totalSum*(r-l+1)
            # print('Score,r,l',score,r,l)
                # we need to caculate subarray for the prev and reset everything
            while score>=k and l<=r:
                totalSum-=nums[l]
                l+=1
                score = totalSum*(r-l+1)
            res += (r-l+1)
            r+=1

        # print('R,L',r,l,res)
        return res