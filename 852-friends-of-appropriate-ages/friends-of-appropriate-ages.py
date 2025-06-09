class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = len(ages)
        count = 0
        freq = Counter(ages)
        for a in range(1,121):
            for b in range(1,121):
                if not freq[a] or not freq[b]:
                    continue
                if b<=0.5*a+7 or b>a or (b>100 and a<100):
                    continue
                if a==b:
                    count+= freq[a]*(freq[b]-1)
                else:
                    count+= freq[a]*freq[b]
        
        return count
