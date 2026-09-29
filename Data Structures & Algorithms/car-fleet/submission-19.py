class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
       
        arrivalTimes = []
        for pos, spd in cars:
            arrivalTime = (target-pos) / spd
    
            if arrivalTimes and arrivalTimes[-1] >= arrivalTime:
                continue
               
            arrivalTimes.append(arrivalTime)
        return len(arrivalTimes)