# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if head == None:
            return 0
        ans = 0
        now = head
        G = set(G)
        while now != None:
            if now.next != None:
                if now.val in G and now.next.val not in G:
                    # set  基于hash，所有基于hash的，查找都是O(1)，
                    #list 基于数组，查找O(N)
                    ans+=1
            else:
                if now.val in G:
                    ans +=1
            now = now.next        
        return ans

