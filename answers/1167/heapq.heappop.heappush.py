from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0
        heapify(sticks)
        ans = 0
        lastOne,lastTwo = 0,0
        while len(sticks) != 1:
            lastOne = heappop(sticks)
            lastTwo = heappop(sticks)
            ans = ans + lastOne + lastTwo
            heappush(sticks,lastTwo+lastOne)

        return ans











            
            





