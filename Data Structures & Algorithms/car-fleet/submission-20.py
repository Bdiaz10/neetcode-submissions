class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        arrivalTimes = []

        for i in range(len(cars)-1,-1,-1):
            arrivalTime = (target-cars[i][0]) / cars[i][1]

            if arrivalTimes and arrivalTime <= arrivalTimes[-1]:
                continue
            arrivalTimes.append(arrivalTime)
        
        return len(arrivalTimes)