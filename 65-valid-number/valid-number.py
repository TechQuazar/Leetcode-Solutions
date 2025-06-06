class Solution:
    def isNumber(self, s: str) -> bool:
        """
        https://leetcode.com/problems/valid-number/solutions/173977/python-with-simple-explanation
        """
        n = len(s)
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i,char in enumerate(s):
            if char in '+-':
                if i>0 and s[i-1].lower()!='e':
                    return False
            elif char =='.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char.lower() =='e':
                if met_e or not met_digit:
                    return False
                met_e,met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit
