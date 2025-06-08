class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        """
        trips.sort(key=lambda x:x[1])
        pq = []
        currPas = 0
        for pas,st,ed in trips:
            while pq and pq[0][0]<=st:
                dropEnd, dropPas = heapq.heappop(pq)
                currPas-=dropPas
            currPas+=pas
            if currPas>capacity:
                return False
            heapq.heappush(pq, (ed, pas))
        return True
