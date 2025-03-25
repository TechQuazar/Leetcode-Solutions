class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        '''
        for horizontal
        go from 0 to ymax
        for each yend encountered check if others are not overlapping -> ystarti<=curr<=yendi for all rectangles i
        if not add separator -> recur on the remaining 
        for linesLeft = 0, check if any of the left ones is intersecting -> O(nlogn) sort by ystart then greedly check
        ----------------\U0001f446 TOO SLOW ---------------------
        Binary search? -> at y check for any overlaps
        ---------------\U0001f446 WRONG ------------------------
        Need a faster solution due to constraints
        sort + overlappings intervals??
        merge intervals that are overlapping? - cause no way to resolve that
        WILL WORK!
        Repeat for horizontal and vertical due to symmetry
        '''
        # horizontal lines first -> along y
        print('Horizontal lines')
        pairs = []
        for _,start,_,end in rectangles:
            pairs.append((start,end))
        
        pairs.sort(key= lambda x: (x[0],x[1])) # start first then end
        print('Pairs',pairs)
        y_max = n # inclusive
        prevStart,prevEnd = 0,0
        mergedPairs = []
        for i in range(len(pairs)):
            if i==0:
                prevStart = pairs[i][0]
                prevEnd = pairs[i][1]
                mergedPairs.append((prevStart,prevEnd))
                continue
            else:
                currStart = pairs[i][0]
                currEnd = pairs[i][1]
                if prevStart<=currStart<prevEnd or prevStart<=currEnd<=prevEnd:
                    # overlap, merge
                    mergedPairs[-1] = (min(prevStart,currStart),max(prevEnd, currEnd))
                    prevStart = min(prevStart,currStart)
                    prevEnd = max(prevEnd, currEnd)
                else:
                    # no overlap, add directly
                    mergedPairs.append((currStart,currEnd))
                    prevStart = currStart
                    prevEnd = currEnd
        print('Merged',mergedPairs)
        if len(mergedPairs)>=3:
            return True
        # vertical lines first -> along x
        print('Vertical lines')
        pairs = []
        for start,_,end,_ in rectangles:
            pairs.append((start,end))
        
        pairs.sort(key= lambda x: (x[0],x[1])) # start first then end
        print('Pairs',pairs)
        y_max = n # inclusive
        prevStart,prevEnd = 0,0
        mergedPairs = []
        for i in range(len(pairs)):
            if i==0:
                prevStart = pairs[i][0]
                prevEnd = pairs[i][1]
                mergedPairs.append((prevStart,prevEnd))
                continue
            else:
                currStart = pairs[i][0]
                currEnd = pairs[i][1]
                if prevStart<=currStart<prevEnd or prevStart<=currEnd<=prevEnd:
                    # overlap, merge
                    mergedPairs[-1] = (min(prevStart,currStart),max(prevEnd, currEnd))
                    prevStart = min(prevStart,currStart)
                    prevEnd = max(prevEnd, currEnd)
                else:
                    # no overlap, add directly
                    mergedPairs.append((currStart,currEnd))
                    prevStart = currStart
                    prevEnd = currEnd
        
        print('Merged',mergedPairs)
        if len(mergedPairs)>=3:
            return True

        return False
