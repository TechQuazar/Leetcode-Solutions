class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        if n==0:
            return []
        if n==1:
            return [1]
        indices = Counter(s)
        i=0
        freq = defaultdict(int)
        res = []
        def isWindowGood():
            for k,v in freq.items():
                if indices[k]!=v:
                    return False
            return True
        
        while i<n:
            curr = s[i]
            freq[curr]+=1
            if indices[curr]==freq[curr]:
                if isWindowGood():
                    res.append(i+1)
                    nextRes = self.partitionLabels(s[i+1:])
                    res.extend(nextRes)
                    return res
            i+=1
    
        return res