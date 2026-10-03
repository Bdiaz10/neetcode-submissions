"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {} # og -> clone
        def createClone(start):
            if start not in copies:
                copies[start] = Node(start.val)
                for n in start.neighbors:
                    copies[start].neighbors.append(createClone(n))
            return copies[start]
       

        return createClone(node) if node else None


            