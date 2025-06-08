class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Stores remainders of prefix sums (modulo k)
        seen_remainders = set()
        
        # Running total (prefix sum)
        total = 0
        
        # Stores the previous remainder to ensure subarray length ≥ 2
        prev_remainder = 0

        for num in nums:
            total += num
            remainder = total % k  # Only matters for multiples

            # If we've seen this remainder before, the subarray in between is divisible by k
            if remainder in seen_remainders:
                return True

            # Store the previous remainder (delayed) to ensure subarray size is at least 2
            seen_remainders.add(prev_remainder)
            prev_remainder = remainder

        return False