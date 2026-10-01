from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:        
        values = self.store[key]
        if not values:
            return ""
        if timestamp < values[0][1]:
            return ""

        left = 0
        right = len(values)-1
        res = ""
        while left <= right:
            middle = left + (right-left)//2

            if values[middle][1] == timestamp:
                return values[middle][0]
            
            if timestamp < values[middle][1]:
                right = middle -1
            else:
                left = middle +1
                res = values[middle][0]
        return res


# [0, 1, 2, 4, 5]
