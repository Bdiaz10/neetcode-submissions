import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n+1)}
        for src, dst, wt in times:
            adjList[src].append((dst, wt))
        
        # store min distance to reach node
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0

        # (currentDistance, node)
        q = [(0, k)]
        while q:
            distance, node = heapq.heappop(q)
            if distance > distances[node]:
                continue
            
            for dst, wt in adjList[node]:
                newWeight = distance + wt
                if newWeight < distances[dst]:
                    distances[dst] = newWeight
                    heapq.heappush(q, (newWeight, dst))
        
        result = max(distances.values())
        return result if result != float('inf') else -1
        