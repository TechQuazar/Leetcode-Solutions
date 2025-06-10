class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ",'')
        op = '+'
        s += '+'
        curr = 0
        st = []
        for ch in s:
            if ch.isdigit():
                curr = curr*10 + int(ch)
            elif ch in '+-*/':
                if op=='+':
                    st.append(curr)
                elif op=='-':
                    st.append(-curr)
                elif op=='*':
                    st.append(st.pop()*curr)
                elif op=='/':
                    st.append(int(st.pop()/curr))
                curr = 0
                op = ch

        return sum(st)
