class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            curr = numbers[i]
            req = target - curr
            l = i+1
            r = n-1
            while l<=r:
                mid = (l+r)//2
                if numbers[mid]==req:
                    return [min(mid+1,i+1),max(mid+1,i+1)]
                elif numbers[mid]<req:
                    l = mid+1
                else:
                    r = mid -1
        