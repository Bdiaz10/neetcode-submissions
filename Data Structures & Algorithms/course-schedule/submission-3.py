from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjlist {0: [1], 1: [0]}
        adjlist = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjlist[course].append(prereq)
        
    
        path = set()
        def canComplete(course):
            if adjlist[course] == []:
                return True
            if course in path:
                return False
            path.add(course)
            for prereq in adjlist[course]:
                if not canComplete(prereq):
                    return False
            path.remove(course)
            adjlist[course] = []
            return True
            
            
        for course in adjlist.keys():
            if not canComplete(course):
                return False
        return True
        

