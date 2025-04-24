class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(int)
        for i,x in enumerate(nums):
            if target-x in lookup:
                return [i, lookup[target-x]]
            lookup[x] = i