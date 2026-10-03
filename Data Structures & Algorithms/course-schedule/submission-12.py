class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        cycle = set()
        completed = set()
        def hasCycle(course) -> bool:
            if course in cycle:
                return True
            if course in completed:
                return False
            cycle.add(course)
            for prereq in graph[course]:
                if hasCycle(prereq):
                    return True
            cycle.remove(course)
            completed.add(course)
            return False
        
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True
        