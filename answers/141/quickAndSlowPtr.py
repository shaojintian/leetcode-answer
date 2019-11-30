# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if  head ==None :
            return False
        if head.next != None:
            slow = head.next
            quick = head.next.next
        else :
            return False    
        while quick != None and slow != None:
            if slow == quick:
                return True
            if quick.next == None:
                return False
            else:        
                quick = quick.next.next

            slow = slow.next                           

        return  False

