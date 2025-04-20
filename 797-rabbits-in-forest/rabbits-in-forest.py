class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        '''
        decision tree logic
        [1 1 2]
        1 -> col red
        1 -> either red or diff (yellow).  If diff then it must have one with same col later
        2 -> can be red -> then one more red. can't be yellow cause then it means we need 1 more yellow but idx 1 already said only one more yellow. Can be new col => blue then 2 + blue
        need to assign id to each idx for color identification
        0:1 -> 0 and set the max count of color 0 to be 1+ val[idx] = 1+ val[0] = 2. currCount[0] = 1
        1:1 -> check for val in colorCount. If any val == 1, make it 2 and recur
        2:2 -> 0 or 2

        # greedy logic will work -> eliminate common pairs
        For min, if curr 1, we try to match it with prev 1
        sim if we have 1 2, we cant match 2 with 1
        if we have seq 1 2 3 4 5 
        1 1 contained pair
        2 2 2 -> contained pair
        3 3 3 3=> val+1 items are contained pairs
        we need contained pairs, if we can form naturally then best else add to res
        like if we have 3 3 => we need 2 more 3, else we need to add 2 to res
        '''
        n = len(answers)
        currCount = [0]*1000 # max 1000 values, each can have uniq
        maxCount = [0]*1000
        answers.sort() # keep ordered 

        # def recur(i,currCount, maxCount, colorIdx):
        #     if i==n:
        #         return 0
        #     res = float('inf')
        #     #check if previously available
        res = 0
        i = 0
        while i<n:
            curr = answers[i]
            pairCount = curr+1 # must be these many for curr to satisfy min
            count = 0
            while i<n-1 and curr==answers[i+1]:
                count+=1
                if count==pairCount:
                    res+=pairCount
                    count=0
                i+=1
            if count<pairCount:
                res+= pairCount
            i+=1
        
        return res


        
        # return recur(0,currCount, maxCount,0)
