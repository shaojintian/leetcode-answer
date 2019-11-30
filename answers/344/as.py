class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)//2
        low = 0
        high = len(s) -1
        while low < high:
            tmp = s[low]
            s[low] = s[high]
            s[high] = tmp
            low+=1
            high-=1