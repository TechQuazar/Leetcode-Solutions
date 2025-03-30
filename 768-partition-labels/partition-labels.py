from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        preprocessing -> in order
        for i in range(n) -> at each i check whats the count of that char
        If == total count, partition it
        Do the same for all the chars in that window
        works cause going in order, if u encounter a char, you cant stop window till its count ==0 else it wont be possible to split
        '''
        l,r=0,0
        n = len(s)
        totalCount = Counter(s)
        window = defaultdict(int)
        currLen = 0
        res = []
        while r<n:
            curr = s[r]
            currLen+=1
            window[curr]+=1
            isValid = True
            for k,v in window.items():
                if totalCount[k]!=window[k]:
                    isValid=False
                    break
            if isValid:
                window = defaultdict(int)
                res.append(currLen)
                currLen = 0
            r+=1
        return res
