class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prod = []
        self.zeroIdx = []
        

    def add(self, num: int) -> None:
        self.arr.append(num)
        if len(self.prod)==0:
            self.prod.append(num)
            if num==0:
                self.zeroIdx.append(0)
        else:
            if num!=0:
                if (len(self.zeroIdx)>0 and self.zeroIdx[-1]!=len(self.arr)-2) or len(self.zeroIdx)==0:
                    self.prod.append(num*self.prod[-1])
                else:
                    self.prod.append(num)
            else:
                self.prod.append(num)
                self.zeroIdx.append(len(self.arr)-1)
        # print('arr',self.arr)
        # print('prod',self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.zeroIdx)==0:
            if k==len(self.prod):
                return self.prod[-1]
            return self.prod[-1]//self.prod[len(self.prod)-k-1]
        else:
            lastIdx = self.zeroIdx[-1]
            # print('lastIdx',lastIdx)
            # print('K',k)
            if len(self.prod)-k <= lastIdx:
                return 0
            else:
                denom = self.prod[len(self.prod)-k-1]
                if denom==0:
                    denom = 1
                return self.prod[-1]//denom


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)