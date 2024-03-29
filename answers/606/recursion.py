# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ""
        if t.left == None and t.right == None:
            return str(t.val)
        if t.left != None  and t.right == None:
            return str(t.val)+'('+self.tree2str(t.left)+')'    

        return str(t.val)+'('+self.tree2str(t.left)+')('+self.tree2str(t.right)+')'




