"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        curr = 0
        res = 0

        i = 0
        j = 0
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                curr += 1
            else:
                j += 1
                curr -= 1
            res = max(curr, res)
        return res

