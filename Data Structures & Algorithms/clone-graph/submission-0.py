"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.seen_set = dict()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        if node.val in self.seen_set:
            return self.seen_set[node.val]
        
        new_node = Node()
        new_node.val = node.val
        self.seen_set[node.val] = new_node 
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        return new_node

        