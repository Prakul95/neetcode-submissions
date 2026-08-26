# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = float("-inf")
        max_val = float("inf")

        if not root:
            return True
        q = deque()
        q.append([min_val, max_val, root])

        while q:
            for _ in range(len(q)):
                min_val, max_val, node = q.popleft()
                if not node:
                    continue
                if min_val<node.val<max_val:
                    q.append([min_val, node.val, node.left])
                    q.append([node.val, max_val, node.right])
                else:
                    return False
        return True
