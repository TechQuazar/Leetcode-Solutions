class Solution:
    def countLargestGroup(self, n: int) -> int:
        sizeMap = defaultdict(int)
        def digitSum(num):
            res = 0
            while num>0:
                rem = num%10
                num = num//10
                res+=rem
            return res
        maxSize = 0
        for i in range(1,n+1):
            currSum = digitSum(i)
            sizeMap[currSum]+=1
            if sizeMap[currSum]>maxSize:
                maxSize = sizeMap[currSum]
        res = 0
        for k,v in sizeMap.items():
            if v==maxSize:
                res+=1
        return res