class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        """
        state tracking. Repeat till you encounter same state twice -> maybe set or a flag to see changes
        1. if ast -> no collision from left side
        2. if ast -> and right ->, no collision
        3. if ast -> and right <-, collision, 

        for each keep a temp[] to track new state
        """
        while True:
            i = 0
            temp = []
            noChange = True
            n = len(ast)
            while i<n:
                # collision on right
                if i+1<n and (ast[i]>0 and ast[i+1]<0):
                    if abs(ast[i])>abs(ast[i+1]):
                        temp.append(ast[i])
                    elif abs(ast[i])<abs(ast[i+1]):
                        temp.append(ast[i+1])
                    noChange = False
                    i+=1
                else:
                    temp.append(ast[i])
                i+=1
            if noChange:
                return temp
            ast = temp
        return []

