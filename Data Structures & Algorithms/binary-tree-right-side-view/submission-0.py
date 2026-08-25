# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        res = []
        if not root:
            return []
        
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            temp = None
            for _ in range(0, n):
                node = q.popleft()
                if not node:
                    continue
                temp = node
                q.append(node.left)
                q.append(node.right)
            
            if temp:
                res.append(temp.val)
        return res
                