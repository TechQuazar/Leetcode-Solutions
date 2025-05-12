class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        evenDigits = set()
        for x in digits:
            if x%2==0:
                evenDigits.add(x)
        # choose last place from evenDigits
        counter = Counter(digits)
        res = set()
        for last in evenDigits:
            counter[last]-=1
            for second in digits:
                counter[second]-=1
                for first in digits:
                    counter[first]-=1
                    if counter[first]>=0 and counter[second]>=0 and counter[last]>=0 and first!=0:
                        res.add(first*100 + second*10 + last)
                    counter[first]+=1
                counter[second]+=1
            counter[last]+=1
        return sorted(list(res))