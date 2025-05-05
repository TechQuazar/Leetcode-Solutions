class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l,r = 0,n-1
        counter = 0
        while l<r:
            if people[l]+people[r]<=limit:
                counter+=1
                l+=1
                r-=1
            else:
                r-=1
        return n-counter