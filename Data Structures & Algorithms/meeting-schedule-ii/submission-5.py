"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort start and end times
        startT = sorted([i.start for i in intervals])
        endT = sorted([i.end for i in intervals])

        days = 0
        curr = 0
        start = 0
        end = 0
        while start < len(startT):
            if startT[start] < endT[end]:
                start += 1
                curr += 1
            else:
                end += 1
                curr -= 1
            days = max(days, curr)
        return days