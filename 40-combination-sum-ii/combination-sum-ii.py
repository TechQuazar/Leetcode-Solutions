class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        n = len(arr)
        res = []
        arr.sort()  # Required for skipping duplicates

        def recur(start, curr, path):
            if curr == target:
                res.append(list(path))
                return
            if curr > target:
                return

            prev = -1  # placeholder for last value used at this depth
            for i in range(start, n):
                if arr[i] == prev:
                    continue  # skip duplicates at same depth
                if curr + arr[i] > target:
                    break
                path.append(arr[i])
                recur(i + 1, curr + arr[i], path)
                path.pop()
                prev = arr[i]

        recur(0, 0, [])
        return res
