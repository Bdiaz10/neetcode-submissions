class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        arrivalTimes = []
        for car in cars:
            timeToTarget = (target - car[0]) / car[1]
            if arrivalTimes and timeToTarget > arrivalTimes[-1] or not arrivalTimes:
                arrivalTimes.append(timeToTarget)
                
        return len(arrivalTimes)