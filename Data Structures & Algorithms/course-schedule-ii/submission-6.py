class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        result = []
        completed = set()
        cycle = set()
        def completeCourse(course: int) -> bool:
            if course in completed:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for prereq in graph[course]:
                valid = completeCourse(prereq)
                if not valid:
                    return False

            cycle.remove(course)
            completed.add(course)
            result.append(course)
            return True
        
        for i in range(numCourses):
            valid = completeCourse(i)
            if not valid:
                return []
        return result