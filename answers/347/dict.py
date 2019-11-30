class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else :
                m[i] += 1
        m = sorted(m.items(),key=lambda x:x[1],reverse = True)
        ans = []
        for i in range(k):
            ans.append(m[i][0]) 
        return ans   




