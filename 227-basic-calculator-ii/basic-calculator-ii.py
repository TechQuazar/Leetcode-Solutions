class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        s = s+'+'
        op = "+"
        st = []
        curr = 0
        for i,ch in enumerate(s):
            if ch.isdigit():
                curr = curr*10 + int(ch)
            elif ch in '+-/*':
                if op=='+':
                    st.append(curr)
                if op=='-':
                    st.append(-curr)
                if op=='*':
                    st.append(st.pop()*curr)
                if op=='/':
                   st.append(int(st.pop()/curr))
                op = ch
                curr = 0
        return sum(st)