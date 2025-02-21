class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        print('nums',nums)
        n = len(nums[0])
        ideal_total = 2**n
        each = ideal_total//2
        if '0'+'1'*(n-1) not in nums:
            return '0'+'1'*(n-1)
        idx = nums.index('0'+'1'*(n-1))
        # print('nums,idx',nums,idx)
        res = ""
        def recur(st):
                nonlocal res
                if len(st)==n:
                    if st not in seen:
                        res = st
                        return True
                    return False
                
                return recur(st+'0') or recur(st+'1')
        arr = []
        if idx <= each-1:
            # its in first half
            arr = nums[:idx+1]
        else:
            arr = nums[idx+1:]
        
        seen = set(arr)
        n = len(arr[0])
        recur('')
        return res


