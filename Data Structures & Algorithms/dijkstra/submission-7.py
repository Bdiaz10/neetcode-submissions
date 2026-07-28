class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Construct the graph
        graph = defaultdict(list)
        for s, d, c in edges:
            graph[s].append((c, d))
        
        # Initialize distances to infinity and the source vertex to 0
        distances = [float('inf')] * n
        distances[src] = 0

        # Initialize the priority queue (min heap) with the source vertex
        minheap = []
        heapq.heappush(minheap, (0, src))

        # Dijkstra's algorithm
        while minheap:
            # Pop the node with the smallest tentative distance
            cost, node = heapq.heappop(minheap)

            # Update the distances to its neighbors
            for neighborCost, neighbor in graph[node]:
                # Update the distance if a shorter path is found
                if cost + neighborCost < distances[neighbor]:
                    distances[neighbor] = cost + neighborCost
                    heapq.heappush(minheap, (distances[neighbor], neighbor))

        # Convert the distances to a dictionary format
        res = {}
        for i in range(len(distances)):
            res[i] = distances[i] if distances[i] != float('inf') else -1

        return res