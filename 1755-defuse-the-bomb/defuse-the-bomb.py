class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n
        if k==0:
            return res
        incr = 1 if k>0 else -1
        curr_sum = 0
        for j in range(0,k,incr):
            curr_sum += code[j+incr]
        idx = 0
        while abs(idx)<n:
            if idx==0:
                res[idx] = curr_sum
            else:
                curr_sum = curr_sum - code[idx] + code[(idx+k)%len(code)]
                res[idx] = curr_sum
            idx+=incr
        return res
