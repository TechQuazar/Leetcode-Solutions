class Solution:
    def numTilings(self, n: int) -> int:
        '''
        2 rows
        tiles are identical, need to change layout for uniqness
        tromino -> 2 patters given in ex1, plus 2 patters of dom bw trom ends, plus 2 patters of dom bw same face
        trom ends. Any trom in between trom ends has to be paired with other trom to close the gap.
        domino -> same three patterns
        ----
        -**-
        some sort of fix till i, then independently solve i+1 to n
        recursion
          1
        1 1
        |--, |||, --|
        BFE - dom patters + trom patters
        --OPT
        0 = 1, N=0 return 0
        1: [|] 2:[--, |], 3: [--|,|--,|||, trom1, trom2] == [dp[2]+[|], dp[1]+[--], dp[0]+[trom1, trom2]]
        dp[4] = [dp[3]+[|], dp[2]+[--], dp[1]+[trom1,trom2],dp[0]+[<->, <->]]

        dp[n] = dp[n-1] + dp[n-2] + 2*(dp[n-3] + dp[n-4] +...+ dp[0])
              = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-3] + 2*(dp[n-4]+...)
              = dp[n-1] + dp[n-3] + (dp[n-2]+dp[n-3]+ 2*(dp[n-4]+...)])
              = 2*dp[n-1] + dp[n-3]
        '''
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        MOD = 10**9 + 7
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = 2*dp[i-1] + dp[i-3]
            dp[i] = dp[i]%MOD
        return dp[n]%MOD

                    