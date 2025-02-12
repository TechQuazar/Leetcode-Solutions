class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 43 36 18 13 7
        # 7  9  9  4  7
        res = -1
        nums.sort(reverse=True)
        # print("sorted nums:",nums)
        def digitSum(num):
            res = 0
            while num>0:
                res+= num%10
                num = num//10
            return res

        sum_arr = [digitSum(x) for x in nums]
        # print("sum_arr",sum_arr)

        sum_pairs = defaultdict(list)
        for i,x in enumerate(sum_arr):
            sum_pairs[x].append(i)
        
        for k,v in sum_pairs.items():
            if len(v)<2:
                continue
            res = max(res, nums[v[0]]+nums[v[1]])
        
        return res

