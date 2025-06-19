class Solution:
    def intToRoman(self, num: int) -> str:
        valToSym = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        res = []
        base = 1
        # 3749 -> "MMMDCCXLIX"
        while num>0:
            d = num%10
            curr = base* d
            num = num//10
            if d==4 or d==9:
                res.append(valToSym[base]+valToSym[curr+base])
            else:
                temp = ""
                if d!=5:
                    if d>5:
                        d = d-5
                        temp+= valToSym[5*base]
                    temp += d*valToSym[base]
                else:
                    temp = valToSym[curr]
                res.append(temp)
            base = base*10

        return ''.join(res[::-1])