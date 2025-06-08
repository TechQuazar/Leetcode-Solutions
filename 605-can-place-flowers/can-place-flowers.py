class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        m = len(arr)
        if m==1 and arr[0]==0:
            if n<=1:
                return True
            return False
        i = 0
        while i<m:
            if i==0 and i+1<m and arr[i]==0 and arr[i+1]!=1:
                n-=1
                i+=1
            elif arr[i]==0 and i-1>=0 and arr[i-1]!=1 and i+1<m and arr[i+1]!=1:
                n-=1
                i+=1
            elif i==m-1 and arr[i]==0 and i-1>=0 and arr[i-1]!=1:
                n-=1
                i+=1
            i+=1
        return n<=0

