import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i : [] for i in range(1, n+1)}
        for src, dst, wt in times:
            adjList[src].append((dst, wt))

        # min distance to reach node from k
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0

        # current distance, node
        q = [(0, k)]
        while q:
            currentDistance, node = heapq.heappop(q)
            if currentDistance > distances[node]:
                continue
            
            for neighbor, wt in adjList[node]:
                newDistance = currentDistance + wt
                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance
                    heapq.heappush(q, (newDistance, neighbor))
        
        res = max(distances.values())
        return res if res != float('inf') else -1