"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       
        adjList = {}
        def buildAdjList(start):
            if start in adjList or not start:
                return
            adjList[start] = Node(start.val)
            for n in start.neighbors:
                buildAdjList(n)
        
        buildAdjList(node)
        print(adjList)

        seen = set()
        def buildGraph(start):
            if not start or start in seen:
                return None
            seen.add(start)
            copy = adjList[start]
            for neighbor in start.neighbors:
                copy.neighbors.append(adjList[neighbor])
                buildGraph(neighbor)
            return copy
        
        return buildGraph(node)


       



