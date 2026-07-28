from collections import defaultdict
import heapq
class TimeMap:

    def __init__(self):
        # {key: [(time, value)]} sorted by time reversed
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # heapq.heappush(self.store[key], (timestamp, value))
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or self.store[key] == []:
            return ""
        # binary search for the largest value <= timestamp
        left = 0
        right = len(self.store[key])-1
        maxValue = [(0,'')]
        while left <= right:
            middle = (left + right) // 2
            if self.store[key][middle][0] > timestamp:
                right = middle -1
            elif self.store[key][middle][0] < timestamp:
                left = middle + 1
                if self.store[key][middle][0] > maxValue[0][0]:
                    maxValue[0] = (self.store[key][middle][0], self.store[key][middle][1])
            else:
                return self.store[key][middle][1]

        return maxValue[0][1]

        
