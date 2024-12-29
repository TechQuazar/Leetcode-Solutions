class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)
        cache = {}
        freq = defaultdict(lambda: defaultdict(int))
        def recur(i,j):
            nonlocal res
            if j==n:
                return 1
            if i>=m:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            total = 0
            curr = ord(target[j]) - ord('a')
            # total+=recur(i+1,j)
            total+=recur(i+1,j)%MOD
            total+= freq[i][curr]*recur(i+1,j+1)
            cache[(i,j)] = total%MOD
            return total%MOD

        for i,word in enumerate(words):
            for j in range(m):
                currPos = ord(word[j]) - ord('a')
                freq[j][currPos]+=1
        res = recur(0,0)
        return res%MOD
        '''
        acca bbbb caca

        '''