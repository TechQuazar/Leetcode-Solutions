class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        can we do it at all? n = len(tops)
        - count the occurrences of all digits. If its >=n, we check if that digit is present in each domino and its
        not just duplicates.
        - Yes, then that is what we need.
        - At most, there might be 2 values of occurrences when count==n, and we need to check both
        checking each is O(n)
        counting occurrences is O(n + n*k) where k is the count of values >=n
        Overall O(n)
        """
        n = len(tops)
        freq = defaultdict(int)
        for i in range(n):
            freq[tops[i]]+=1
            freq[bottoms[i]]+=1
        
        possible = []
        for k,v in freq.items():
            if v>=n:
                possible.append(k)

        isGood = []
        for val in possible:
            flag = False
            for i in range(n):
                if tops[i]!= val and bottoms[i]!=val:
                    flag = True
                    break
            if not flag:
                isGood.append(val)
        # print('possible',possible)                   
        # print('isGood',isGood)
        if len(isGood)==0:
            return -1
        res = n
        for val in isGood:
            countTops = 0
            countBots = 0
            for i in range(n):
                if tops[i]==val:
                    countTops+=1
                if bottoms[i]==val:
                    countBots+=1
            res = min(n-countTops, n-countBots, res)
        
        return res