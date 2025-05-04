class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        '''
        1. at idx, is curr + val[idx]<=target? go for it
        2. Additionally, just skip it cause you can
        3. base when target==0 add to set
        4. maintain set to ensure uniq answers
        '''
        n = len(arr)
        res = set()
        def recur(i,curr, path):
            nonlocal res
            if curr==target:
                res.add(path)
                return
            if i>=n or curr>target:
                return
            if curr+arr[i]<=target:
                # print('i,curr,path',i,curr,path)
                newPath = list(path)
                newPath.append(arr[i])
                recur(i,curr+arr[i],tuple(newPath))
            # print('out:i,curr,path',i,curr,path)
            recur(i+1,curr,path)
        
        recur(0,0,())
        ans = []
        for each in res:
            ans.append(list(each))
        return ans