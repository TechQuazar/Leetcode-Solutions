class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = ''
        n = len(pattern)
        def recur(i, st):
            nonlocal res
            if i==n:
                res = st
                return True
            curr = pattern[i]
            # print('i,st,curr',i,st,curr)
            for num in range(1,10):
                if str(num) in st:
                    continue
                if st=='':
                    if (recur(i+1,st+str(num))):
                        return True
                else:
                    if curr=='I' and num>int(st[-1]):
                        if(recur(i+1,st+str(num))):
                            return True
                    if curr=='D' and num<int(st[-1]):
                        if(recur(i+1,st+str(num))):
                            return True
            return False

        if pattern[0]=='I':
            res+='1'
            recur(0,'1')
        else:
            recur(-1,'')

        return res