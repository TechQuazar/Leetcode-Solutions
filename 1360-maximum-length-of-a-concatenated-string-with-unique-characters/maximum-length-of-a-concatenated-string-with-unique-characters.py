class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # ignore all strings in arr that are not uniq themselves
        # at each idx, i can take the substring if it doesnt interfere or i can leave
        # recursion will return the length of longest uniq that can be formed
        newList = []
        for s in arr:
            temp = [0]*26
            ignore = False
            for ch in s:
                x = ord(ch)-ord('a')
                temp[x]+=1
                if temp[x]>=2:
                    ignore = True
                    break
            if not ignore:
                newList.append(temp)
        arr = newList
        n = len(arr)
        cache = {}
        def recur(i, currStr):
            if i==n:
                return 0
            # take if no interference with prev
            if (i,currStr) in cache:
                return cache[(i,currStr)]
            res = 0
            take,leave = 0,0
            ignore = False
            for j,x in enumerate(arr[i]):
                if currStr[j]>0 and x>0:
                    ignore = True
                    break
            if not ignore:
                count = 0
                temp = list(currStr)
                for j,x in enumerate(arr[i]):
                    if x>0:
                        count+=1
                        temp[j]+=1
                take = count + recur(i+1,tuple(temp))
            leave = recur(i+1,tuple(currStr))
            cache[(i,currStr)] = max(take,leave)
            return cache[(i,currStr)]
        
        return recur(0,tuple([0]*26))

