class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        s = s+'+'
        op = "+"
        prevNum = 0
        res = 0
        curr = 0
        for i,ch in enumerate(s):
            if ch.isdigit():
                curr = curr*10 + int(ch)
            elif ch in '+-/*':
                if op=='+':
                    res+= prevNum
                    prevNum = curr
                if op=='-':
                    res+= prevNum
                    prevNum = -curr
                if op=='*':
                    # res+= prevNum*curr
                    prevNum = prevNum*curr
                if op=='/':
                    # res+= int(prevNum/curr)
                    prevNum = int(prevNum/curr)
                op = ch
                curr = 0
        return res+prevNum