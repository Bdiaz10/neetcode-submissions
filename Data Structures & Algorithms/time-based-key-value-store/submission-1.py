from collections import defaultdict
class TimeMap:

    def __init__(self):
        # {key: [(time, value)]} sorted by time reversed
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        self.store[key].sort(reverse=True)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or self.store[key] == []:
            return ""
        for i, v in enumerate(self.store[key]):
            if v[0] <= timestamp:
                return v[1]
        return ""
        
