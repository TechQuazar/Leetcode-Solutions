class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        '''
        when encountered an element that is out of bounds, essentially the prev subarrays are useless
        drop them and start new from the next idx

        '''
        res = 0
        l,r = 0,0
        start = 0
        end = 0
        isMinPresent = False
        minIndices = []
        isMaxPresent = False
        maxIndices = []
        n = len(nums)
        def findMinIndices(minIndices, maxIndices):
            return [min(minIndices[-1], maxIndices[-1]), max(minIndices[-1], maxIndices[-1])]

        # for duplicates of minK and maxK, we need their indices start,end such that |start-end| is minimum
        while r<n:
            curr = nums[r]
            if minK<=curr<=maxK:
                if curr==minK:
                    isMinPresent = True
                    minIndices.append(r)
                if curr==maxK:
                    isMaxPresent = True
                    maxIndices.append(r)
                if isMinPresent and isMaxPresent:
                    start, end = findMinIndices(minIndices, maxIndices)
                    res += (start - l + 1)

                r+=1
            else:
                minIndices = []
                maxIndices = []
                isMinPresent = False
                isMaxPresent = False
                r+=1
                l=r
        # print('minIn',minIndices)
        # print('maxIn',maxIndices)

        return res