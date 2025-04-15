from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Sol. We want to fix nums1 as 0 1 2 ... n-1 then remap nums2 accordingly
        This way, the problem is reduced to finding number of increasing position triples in nums2. We don't need to worry about nums1 as any triplet we choose in nums2 is gonna be increasing in position in nums1
        We consider each x in the new nums2 as a middle element, and try to find the elemts smaller than that on left and bigger than that on right. The total would be the product of them
        '''
        n = len(nums1)
        mapping = {}
        for i,x in enumerate(nums1):
            mapping[x] = i
        arr = []
        for x in nums2:
            arr.append(mapping[x])
        nums2 = arr
        # print('nums2',nums2)
        # [1, 2, 0, 3]
        res = 0
        ''' Why SortedList? We want to count the values less than curr. We want to do
        that for each of nums2. Brute force ways are too slow and hard to think of.
        You could try to store the count for each by preprocessing, but that would take O(n^2) - O(n) for processing n elements and O(n) for each iteration.
        If you keep a sortedList, you can use binary search to get the number of elements less than curr in log(n) time.
        '''
        seen = SortedList()
        for x in nums2:
            totalElementsLeft = len(seen)
            smaller_left = seen.bisect_left(x)
            totalBiggerElements = n-1 - x
            totalBiggerLeft = totalElementsLeft - smaller_left
            bigger_right = totalBiggerElements - totalBiggerLeft
            res+= smaller_left*bigger_right
            seen.add(x)
        return res