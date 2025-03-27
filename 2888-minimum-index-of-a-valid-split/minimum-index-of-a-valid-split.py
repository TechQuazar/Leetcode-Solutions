from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        sorting + binary search
        [2,1,3,1,1,1,7,1,2,1]
        [1 1 1 1 1 1 2 2 3 7]
        is mid valid? if yes reduce r to r-mid else increase l to l+mid
        ----------\U0001f446 Rearranges the array - NOT POSSIBLE-------------
        get dom in O(n) time
        preprocess # dom at each index
        ----------\U0001f446 GOT Question Wrong. Same dominant element can be diff for each subarray--------
        O(n) front and back pass to get the dom element from left and right for each idx

        '''
        n = len(nums)
        dom = 0
        maxVal = 0
        # count = Counter(nums)
        # for k,v in count.items():
        #     if v>maxVal:
        #         dom=k
        #         maxVal = v
        currDom = -1
        currDomCount = -1
        count = defaultdict(int)
        idxInfo = [(-1,-1)]*(n-1)
        for i in range(n-1):
            curr = nums[i]
            count[curr]+=1
            if count[curr]>currDomCount:
                currDom = curr
                currDomCount = count[curr]
                if currDomCount>(i+1)/2:
                    idxInfo[i] = (currDom, idxInfo[i][1])
                else:
                    idxInfo[i] = (-1, idxInfo[i][1])
            elif count[curr]==currDomCount:
                idxInfo[i] = (-1, idxInfo[i][1])
            else:
                if currDomCount>(i+1)/2:
                    idxInfo[i] = (currDom, idxInfo[i][1])
                else:
                    idxInfo[i] = (-1, idxInfo[i][1])
        # print('IdxInfo',idxInfo)
        currDom = -1
        currDomCount = -1
        count = defaultdict(int)
        for i in range(n-1,0,-1):
            curr = nums[i]
            count[curr]+=1
            if count[curr]>currDomCount:
                currDom = curr
                currDomCount = count[curr]
                # print('idx,currDom,currDomCount',i,currDom,currDomCount)
                if currDomCount>(n-i)/2:
                    idxInfo[i-1] = (idxInfo[i-1][0],currDom)
                else:
                    idxInfo[i-1] = (idxInfo[i-1][0],-1)
            elif count[curr]==currDomCount:
                idxInfo[i-1] = (idxInfo[i-1][0],-1)
            else:
                if currDomCount>(n-i)/2:
                    idxInfo[i-1] = (idxInfo[i-1][0],currDom)
                else:
                    idxInfo[i-1] = (idxInfo[i-1][0],-1)
        # print('IdxInfo',idxInfo)
        for i in range(n-1):
            a,b = idxInfo[i]
            if a==-1 or b==-1 or a!=b:
                continue
            return i
        return -1
        