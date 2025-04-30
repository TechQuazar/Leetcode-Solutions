class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        BFE - keep a window with count for each char. another base char coutner for t
        go though s in O(N) time, then to check if window is valid in O(52) time => overall O(N*52)
        from all found, get min -> O(X) time
        OPT - O(52) can be reduced by keeping a counter that tracks the uniq elements that satisfy
        the uniq elements and their count in base
        '''
        n = len(s)
        m = len(t)
        if m>n:
            return ""
        base = Counter(t)
        window = defaultdict(int)
        uniq_base = len(base.keys())
        uniq_curr = 0
        l=0
        res = []
        # window_set = set()
        for r in range(n):
            curr = s[r]
            window[curr]+=1
            if curr in base and window[curr]==base[curr]:
                uniq_curr+=1
                # window_set.add(curr)
            if uniq_curr==uniq_base:
                while l<=r and (s[l] not in base or window[s[l]]>base[s[l]]):
                    window[s[l]]-=1
                    if window[s[l]]==0:
                        del window[s[l]]
                    l+=1

                res.append((r-l+1,s[l:r+1]))
                # shrink the window till it becomes invalid
                window[s[l]] -= 1
                if s[l] in base and window[s[l]] < base[s[l]]:
                    uniq_curr -= 1
                l += 1

        # print('Res',res)
        # print('base',base, uniq_base)
        minLen = float('inf')
        ans = ""
        for lenSt, st in res:
            if lenSt<minLen:
                minLen = lenSt
                ans = st
        return ans