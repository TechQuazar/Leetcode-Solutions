class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        2 heaps, similar to one other problem that has to use both min and max heap
        """
        maxHeap = [] # stores the left side of the sorted arr
        minHeap = [] # stores the right side of the sorted arr
        heapDict = defaultdict(int)
        # [1 "2" "3" 4] , [1 "-1" -2 2 3] ; max heap always GTE minHeap
        # [1,3,-1,-3,5,3,6,7] -> [-3 -1] [1 3]
        n = len(nums)
        res = []
        for i in range(k):
            heapq.heappush(maxHeap,-nums[i])
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            if len(minHeap) > len(maxHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        if k%2==1:
            res.append(-maxHeap[0])
        else:
            res.append((-maxHeap[0]+minHeap[0])/2)

        for i in range(k,n):
            prev = nums[i-k]
            # need to remove prev
            heapDict[prev] +=1 # lazy removing. Keep track for now
            
            # now balance - heaps same values or maxHeap has at most 1 more val than minHeap
            balance = -1 if prev<=res[-1] else 1
            # either prev is in maxHeap, meaning we might have equal or 1 less element in maxHeap
            # or prev is in minHeap, meaning we might have one or two more elements in maxHeap
            
            # now process curr num
            if nums[i]<=res[-1]:
                balance +=1
                heapq.heappush(maxHeap,-nums[i])
            else:
                balance -=1
                heapq.heappush(minHeap,nums[i])

            # now balance the heap if balance!=0

            # means max heap has less elements, get from minHeap
            if balance<0:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
            elif balance>0:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            
            # now cleanup maxHeap and minHeap - Lazy removal
            while maxHeap and heapDict[-maxHeap[0]]>0:
                heapDict[-maxHeap[0]]-=1
                heapq.heappop(maxHeap)

            while minHeap and heapDict[minHeap[0]]>0:
                heapDict[minHeap[0]]-=1
                heapq.heappop(minHeap)

            if k%2==1:
                res.append(-maxHeap[0])
            else:
                res.append((-maxHeap[0]+minHeap[0])/2)
 
            
        
        return res