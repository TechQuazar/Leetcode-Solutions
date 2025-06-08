class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        c = 1
        missing = 0
        n = len(arr)
        while True:
            if i<n and arr[i]==c:
                i+=1
            else:
                missing+=1
                if missing==k:
                    return c
            c+=1
    
        


            