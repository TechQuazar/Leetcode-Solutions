class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        '''
        i*j % k=> i%k==0 or j%k==0 or i*j %k==0
        * using gcd. Store all indices for same number. Find all the divisors of k
        starting from indices, add all the divisors of k that can be formed from val
        using gcd, we can find the values that are needed to make the whole divisible by k
        '''
        n = len(nums)
        res = 0
        indices = defaultdict(list)
        divisors = []
        for i in range(1, int(k**0.5)+1):
            if k%i==0:
                divisors.append(i)
                #! we need dividend as well
                if i!=k//i:
                    divisors.append(k//i)

        for i,x in enumerate(nums):
            indices[x].append(i)
        
        res = 0
        for key in indices.keys():
            freq = defaultdict(int)
            for i in indices[key]:
                gcd_i = math.gcd(i,k)
                needed = k//gcd_i
                res+= freq[needed]
                for d in divisors:
                    if i%d==0:
                        freq[d]+=1

        return res