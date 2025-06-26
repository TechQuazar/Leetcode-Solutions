class Solution:
    def findMedianSortedArrays(self,A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half - i

            ALeft  = A[i - 1] if i > 0 else float('-inf')
            ARight = A[i]     if i < m else float('inf')
            BLeft  = B[j - 1] if j > 0 else float('-inf')
            BRight = B[j]     if j < n else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 0:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                else:
                    return min(ARight, BRight)
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1