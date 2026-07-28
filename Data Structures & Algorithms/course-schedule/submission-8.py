class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjlist[course].append(prereq)
        
        path = set()
        completed = set()
        def canComplete(course: int) -> bool:
            if course in completed:
                return True
            if course in path:
                return False
            if adjlist[course] == []:
                return True
            path.add(course)
            for prereq in adjlist[course]:
                if not canComplete(prereq):
                    return False
            path.remove(course)
            completed.add(course)
            return True
            
        for course in adjlist.keys():
            if not canComplete(course):
                return False
        return True