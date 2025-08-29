class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        1. 2 sets of flowers to choose from
        2. The person to choose the last flower must be Bob => keeping a global flower counter
        - At each step, choice bw choosing set1 or set2.
        - If only 1 set remains, T total flowers, if T is odd, current player picks the last flow =>
        if T is odd, and curr player is Bob -> alice wins
        if T is even, and curr player is Alice -> alice wins
        - If 2 sets, X,Y => if Y is odd -> need X to be even
        => if Y is even -> need X to be X odd

        given n,m => [1,2,3,...n] and [1,2,3,...m]
        even choices in x => n//2 --> odd choices in y => m - m//2
        odd choices in x => n - n//2 --> even choices in y => m//2
        eg. n=3, m=2
        1*1 + 2*1 => 3
        """
        return (n//2)*(m-m//2) + (n-n//2)*(m//2)
