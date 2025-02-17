class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        cache = {}
        def recur(i,total):
            # print('i,tot',i,total)
            res = float('inf')
            if total==amount:
                return 0
            if i>=n or total>amount:
                return float('inf')
            if (i,total) in cache:
                return cache[(i,total)]
            res = min(res,1+recur(i,total+coins[i]), recur(i+1,total))
            cache[(i,total)] = res
            return res

        res = recur(0,0)
        return res if res!=float('inf') else -1