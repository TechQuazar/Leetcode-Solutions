class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        cache={}
        def recur(i,total):
            if total==amount:
                return 1
            if i>=n or total>amount:
                return 0
            if (i,total) in cache:
                return cache[(i,total)]
            # take coin, leave coin
            cache[(i,total)] = recur(i,total+coins[i]) + recur(i+1,total)
            return cache[(i,total)]
        return recur(0,0)