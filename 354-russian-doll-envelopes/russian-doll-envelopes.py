class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort by width asc, height desc
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: Extract heights and find LIS
        heights = [h for _, h in envelopes]
        lis = []

        for h in heights:
            idx = bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)