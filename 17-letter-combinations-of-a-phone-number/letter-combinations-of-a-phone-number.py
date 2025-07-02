class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n==0:
            return []
        dMap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def recur(i,path):
            if i==n:
                res.append(''.join(path))
                return
            
            for ch in dMap[digits[i]]:
                path.append(ch)
                recur(i+1, path)
                path.pop()
            return
        recur(0,[])
        return res
            
