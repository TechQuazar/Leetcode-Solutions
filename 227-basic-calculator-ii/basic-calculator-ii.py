class Solution:
    def calculate(self, s: str) -> int:
        """
        1. ignore spaces
        2. precidence matters
        3. can use 2 stacks, one for num one for op
        4. OR when you see * and /, just calc result. Keep +, - in stack till the end
        3 4
        +
        """
        st1 = []
        st2 = []
        res = 0
        s = s.strip()
        if s[0] == '-':
            s = '0' + s  # e.g., "-3+2" becomes "0-3+2"
        n = len(s)
        i=0
        while i<n:
            x = s[i]
            if x==" ":
                i+=1
                continue
            if x=='+' or x=='-':
                st2.append(x)
            elif x=='*' or x=='/':
                num1 = int(st1[-1])
                st1.pop(-1)
                i+=1
                while i<n:
                    # it can only be a number as s is valid expression
                    if s[i]==' ':
                        i+=1
                        continue
                    else:
                        break
                currNum = s[i]
                while i+1 < n and s[i+1] in '0123456789':
                    currNum += s[i+1]
                    i += 1
                num2 = int(currNum)
                if x=="*":
                    st1.append(num1*num2)
                else:
                    st1.append(int(num1 / num2))
            else:
                # print('i,x',i,x, st1, st2)
                currNum = x
                while i+1<n and s[i+1] in ['1','2','3','4','5','6','7','8','9','0']:
                    currNum+=s[i+1]
                    i+=1
                st1.append(int(currNum))
            i+=1
        # now process all the + and -
        # print('st1,st2',st1,st2)
        while st2:
            op = st2[0]
            st2.pop(0)
            num1 = st1[0]
            # st1.pop(0)
            num2 = st1[1]
            st1.pop(1)
            if op=='+':
                st1[0] = num1+num2
            else:
                st1[0] = num1-num2

        return st1[0]
        
