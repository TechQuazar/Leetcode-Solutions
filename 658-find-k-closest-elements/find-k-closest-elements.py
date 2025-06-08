class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        If A[mid] == A[mid + k], we do not know whether we should move left or right when checking the  absolute value.
So, if you really want to use abs, add logic for arr[mid] == arr[mid + k]
        """
        n = len(arr)
        l = 0
        r = n-k
        while l<r:
            mid = (l+r)//2
            if abs(arr[mid]-x)>abs(arr[mid+k]-x):
                l = mid+1
            elif arr[mid]==arr[mid+k]:
                if x>arr[mid]:
                    l = mid+1
                else:
                    r = mid
            else:
                r = mid
        return arr[l:l+k]

