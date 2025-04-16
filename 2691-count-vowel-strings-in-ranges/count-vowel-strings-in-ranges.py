class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        '''
        valid strs -> o(n) time, n = len(words) - preprocess
        prefix sum logic
        '''
        arr = []
        for word in words:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                arr.append(1)
            else:
                arr.append(0)
        n = len(words)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1]+arr[i])
        # print('prefix',prefix)
        res = []
        for l,r in queries:
            res.append(prefix[r+1]-prefix[l])
        # [0 1 2 3]
        return res  