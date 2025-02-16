
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2 * n - 1  
        arr = [-1] * m  
        used = set()  

        def backtrack(index):
            if index == m:  # If we've placed all numbers correctly
                return True
            
            if arr[index] != -1:  # Skip filled positions
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # Try larger numbers first
                if num in used:
                    continue
                if num == 1:  # Place '1' only once
                    arr[index] = num
                    used.add(num)
                    if backtrack(index + 1):
                        return True
                    arr[index] = -1
                    used.remove(num)
                else:
                    if index + num < m and arr[index + num] == -1:
                        arr[index] = arr[index + num] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        arr[index] = arr[index + num] = -1
                        used.remove(num)

            return False

        backtrack(0)
        return arr
