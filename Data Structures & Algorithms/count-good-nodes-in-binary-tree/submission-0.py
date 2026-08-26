# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        res = 0
        q = deque()
        q.append((root, float("-inf")))
        while q:
            n = len(q)
            for _ in range(n):
                node, max_val = q.popleft()
                if not node:
                    continue
                if node.val>=max_val:
                    max_val = node.val
                    res+=1
                q.append((node.left, max_val))
                q.append((node.right, max_val))
        return res
