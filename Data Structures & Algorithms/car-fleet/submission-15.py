class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        arrivalTimes = []
        for pos, spd in cars:
            timeToTarget = (target - pos) / spd
            if arrivalTimes and timeToTarget > arrivalTimes[-1] or not arrivalTimes:
                arrivalTimes.append(timeToTarget)
        return len(arrivalTimes)
        