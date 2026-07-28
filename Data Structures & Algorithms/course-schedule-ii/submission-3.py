class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjlist[course].append(prereq)
        
        path = set()
        completed = set()
        order = []
        def canComplete(course: int) -> bool:
            if course in path:
                return False
            if course in completed:
                return True
            path.add(course)
            for prereq in adjlist[course]:
                if not canComplete(prereq):
                    return False
            path.remove(course)
            completed.add(course)
            order.append(course)
            return True


        for course in adjlist.keys():
            if not canComplete(course):
                return []
        return order