class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert to list to simulate in-place operations
        chars = list(s)
        
        # Step 1: Remove extra spaces in-place
        def remove_extra_spaces(chars):
            n = len(chars)
            i = 0
            while i < len(chars) and chars[i] == ' ':
                i += 1
            chars = chars[i:]  # Remove leading spaces
            
            i = len(chars) - 1
            while i >= 0 and chars[i] == ' ':
                i -= 1
            chars = chars[:i+1]  # Remove trailing spaces
            
            # Now remove multiple spaces between
            i = 0
            res = []
            while i < len(chars):
                if chars[i] != ' ':
                    res.append(chars[i])
                elif res and res[-1] != ' ':
                    res.append(' ')
                i += 1
            return res
        
        chars = remove_extra_spaces(chars)
        
        # Step 2: Reverse the entire list
        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        
        reverse(chars, 0, len(chars) - 1)

        # Step 3: Reverse each word
        n = len(chars)
        start = 0
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                reverse(chars, start, i - 1)
                start = i + 1
        
        return ''.join(chars)
