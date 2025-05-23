class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        n = len(s)
        res = 0
        l=0
        for r in range(n):
            curr = s[r]
            freq[curr]+=1
            # window becomes invalid when we cant fill in the rest of elements with k, wrt max freq element 
            # winLen = r-l+1
            while (r-l+1) - max(freq.values())>k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            res = max(res,r-l+1)

        return res
