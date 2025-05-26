class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {")":"(", "]":"[","}":"{"}
        for ch in s:
            if ch in mapping.values():
                st.append(ch)
            else:
                if not st or st[-1]!=mapping[ch]:
                    return False
                st.pop()
        return True if len(st)==0 else False