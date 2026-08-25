# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        if not root:
            return root
        
        if p and q and p.val>q.val:
            return self.lowestCommonAncestor(root, q,p)
        
        if root and p and q and (p == root or q==root or (p.val<root.val<q.val)):
            return root
        
        if p and root.val>p.val and q and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)