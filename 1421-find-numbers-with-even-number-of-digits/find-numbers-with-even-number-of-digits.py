class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            temp = num
            counter = 0
            while temp>0:
                temp//=10
                counter+=1
            if counter%2==0:
                res+=1

        return res