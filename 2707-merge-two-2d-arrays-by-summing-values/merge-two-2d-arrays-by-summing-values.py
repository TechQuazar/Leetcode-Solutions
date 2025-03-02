class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        h1 = {}
        h2 = {}
        for i,x in nums1:
            h1[i]=x
        for i,x in nums2:
            h2[i]=x
        res = []
        for k,v in h1.items():
            if k in h2:
                res.append([k,v+h2[k]])
            else:
                res.append([k,v])
        for k,v in h2.items():
            if k not in h1:
                res.append([k,v])
        return sorted(res,key = lambda x:x[0])
