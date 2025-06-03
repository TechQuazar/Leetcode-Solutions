class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        res = []
        i,j = 0,0
        m,n = len(a), len(b)
        while i<m and j<n:
            # if a[i] begins before b and no overlap
            if a[i][1]<b[j][0]:
                i+=1

            # if b[j] begins before a and no overlap
            elif b[j][1]<a[i][0]:
                j+=1
            # else a[i] and b[j] overlap
            else:
                start = max(a[i][0],b[j][0])
                end = min(a[i][1],b[j][1])
                res.append([start,end])
                if a[i][1]<b[j][1]:
                    i+=1
                else:
                    j+=1

        return res