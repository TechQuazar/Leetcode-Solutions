from bisect import bisect_left
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        need to keep sorted list
        - sortedcontainer then just median
        - [-1 1 3] bisectleft then insert. window size > k then remove the oldest one
        - how to remove?  we know OG idx, we know which to remove based on curr idx (idx-k)
        - remove based on value. its sorted list so exact removal not required
        """
        arr = []
        q = deque() # store the value to remove
        n = len(nums)
        res = []
        for i in range(n):
            if i==0:
                arr.append(nums[i])
            else:
                idx = bisect_left(arr,nums[i])
                arr.insert(idx,nums[i])
            q.append(nums[i])
            
            if len(arr)>k:
                oldest = q.popleft()
                arr.remove(oldest)
            if len(arr)==k:
                x = len(arr)
                if x%2==0:
                    res.append((arr[x//2]+arr[x//2 - 1])/2)
                else:
                    res.append(arr[x//2])
        return res
                
