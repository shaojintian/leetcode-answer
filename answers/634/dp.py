class Solution:
    def findDerangement(self, n: int) -> int:
        #f(n) = (n-1)*(f(n-1)+f(n-2))
        first = 0
        sec = 1
        if n <=1:
            return 0
        if n==2:
            return 1
        for i in range(3,n+1):
            ans = (i-1)*(sec+first)
            ans = ans %(pow(10,9)+7)
            first = sec
            sec = ans
            

        return ans