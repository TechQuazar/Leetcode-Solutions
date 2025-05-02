class Solution:
    def pushDominoes(self, s: str) -> str:
        '''
        .L.R...LR..L..

        '''
        s = 'L'+s+'R'
        n = len(s)
        res = ""
        i = 0
        for j in range(1,n):
            mid = j-i-1
            if s[j]=='.':
                continue
            if i>0: # append the left domino
                res+=s[i]
            # process middle part
            if s[i]==s[j]:
                res+= s[i]*mid
            elif s[i]=='L' and s[j]=='R':
                res+= '.'*mid
            elif s[i]=='R' and s[j]=='L':
                res+= 'R'*(mid//2) + '.'*(mid%2) + 'L'*(mid//2)
            i=j           

        return res
