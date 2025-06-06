class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if m>n:
            return []
        baseWin = Counter(p)
        currWin = defaultdict(int)
        l,r = 0,0
        res = []
        while r<n:
            curr = s[r]
            currWin[curr]+=1
            # print('currWin',currWin)
            if r-l+1==m:
                if baseWin==currWin:
                    res.append(l)
                currWin[s[l]]-=1
                if currWin[s[l]]==0:
                    del currWin[s[l]]
                l+=1
            r+=1
        return res