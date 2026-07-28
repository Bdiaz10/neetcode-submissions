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
            copy = Node(start.val)
            copies[start] = copy
            for neighbor in start.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy

        return clone(node) if node else None