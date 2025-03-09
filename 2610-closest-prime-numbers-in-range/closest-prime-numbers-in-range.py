class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = []
        def isPrime(x):
            if x==1:
                return False
            if x==2:
                return True
            if x%2==0:
                return False
            for i in range(3,x):
                if x%i==0:
                    return False
            return True
        
        for x in range(left,right+1):
            if isPrime(x):
                if arr and x-arr[-1]<=2:
                    return [arr[-1],x]
                arr.append(x)
            
    
        minDiff = float('inf')
        num1,num2 = -1,-1
        for i in range(len(arr)-1):
            currDiff = arr[i+1]-arr[i]
            if currDiff<minDiff:
                minDiff = currDiff
                num1 = arr[i]
                num2 = arr[i+1]           

        return [num1,num2] if num1!=-1 and num2!=-1 else [-1,-1]