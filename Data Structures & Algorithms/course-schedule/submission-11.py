class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        cycle = set()
        def hasCycle(course) -> bool:
            if course in cycle:
                return True
            cycle.add(course)
            for prereq in adjList[course]:
                if hasCycle(prereq):
                    return True
            cycle.remove(course)
            adjList[course] = []
            return False
        
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True