class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        idx = defaultdict(int)
        for i,x in enumerate(arr):
            idx[x] = i
        n = len(arr)
        cache = {}
        res = 0
        for i in range(n-1):
            for j in range(i+1,n):
                count = 2
                prevIdx = i
                currIdx = j
                # print('i,j',i,j)
                while arr[prevIdx]+arr[currIdx] in idx:
                    # print('prev,curr',arr[prevIdx],arr[currIdx])
                    count+=1
                    res = max(res,count)
                    temp = currIdx
                    currIdx = idx[arr[prevIdx]+arr[currIdx]]
                    prevIdx = temp
        
        return res

                