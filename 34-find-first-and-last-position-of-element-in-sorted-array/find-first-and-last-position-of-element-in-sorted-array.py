class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        if n==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        
        l,r = 0,n-1
        def binary_left(l,r):
            # left end -> either element left of target is diff or target is at idx 0
            while l<r:
                mid = (l+r)//2
                if nums[mid]==target:
                    if (mid-1>=0 and nums[mid-1]!=target) or mid==0:
                        return mid
                    else:
                        r = mid -1
                elif nums[mid]<target:
                    l = mid+1
            if nums[l]==target:
                return l
            return -1

        def binary_right(l,r):
            # right end -> either element right of target is diff or target is at idx n-1
            while l<r:
                mid = (l+r)//2
                if nums[mid]==target:
                    if (mid+1<n and nums[mid+1]!=target) or mid==n-1:
                        return mid
                    else:
                        l = mid+1
                elif nums[mid]>target:
                    r = mid-1
            if nums[l]==target:
                return l
            return -1



        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                a,b=-1,-1
                foundA,foundB = False,False
                if mid-1==-1 or (mid-1>=0 and nums[mid-1]!=target):
                    a = mid
                    foundA = True
                if mid+1==n or (mid+1<n and nums[mid+1]!=target):
                    b = mid
                    foundB = True
                # if left end can be found
                if not foundA and (mid-1>=0 and nums[mid-1]==target):
                    a = binary_left(l,mid-1)

                # if right end can be found
                if not foundB and (mid+1<n and nums[mid+1]==target):
                    b = binary_right(mid+1,r) 
                return [a,b]
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        
        return [-1,-1]