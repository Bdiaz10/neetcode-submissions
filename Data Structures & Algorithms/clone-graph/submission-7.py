"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {} # original -> copy
        def clone(start):
            if start in copies:
                return copies[start]
            copies[start] = Node(start.val)
            for neighbor in start.neighbors:
                copies[start].neighbors.append(clone(neighbor))
            return copies[start]

        return clone(node) if node else None