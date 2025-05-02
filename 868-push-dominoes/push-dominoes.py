class Solution:
    def pushDominoes(self, s: str) -> str:
        """
        .L.R...LR..L..
        LL.RR.LLRRLL..
        BFE - O(n*k) iterate through all keep updating state one by one till you reach same
        OPT - O(k*k) only iterate through the unchanged ones each step of state
        """
        # BFE
        seen  = set()
        n = len(s)
        stable = set()
        print("S",s)
        while True:
            temp = ""
            remain = False
            for i in range(n):
                curr = s[i]
                if curr=='.' and i not in stable:
                    if i==0:
                        # only force from the right one
                        if i+1 <n and s[i+1]=='L':
                            curr="L"
                        elif i+1<n and s[i+1]=='.':
                            remain = True

                    elif i==n-1:
                        # only force from the left one
                        if i-1>=0 and s[i-1]=='R':
                            curr="R"
                        elif i-1>=0 and s[i-1]=='.':
                            remain = True

                    else:
                        # possible force from both
                        if i-1>=0 and i+1<n and s[i-1]=='R' and s[i+1]=='L':
                            curr="."
                        elif i-1>=0 and s[i-1]=='R':
                            curr = 'R'
                        elif i+1<n and s[i+1]=='L':
                            curr = 'L'
                        else:
                            remain = True
                if not remain:
                    stable.add(i)
                temp+=curr
            s = temp
            print('S',s)
            if s in seen:
                return s
            else:
                seen.add(s)
    
        