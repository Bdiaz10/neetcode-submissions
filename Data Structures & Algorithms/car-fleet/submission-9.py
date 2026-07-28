class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # process by closest to finish first (reverse by pos)
        # calculate the time to target, add to stack
        # if current fleet is supposed to reach target at same time, or before the fleet infront, combine them by popping

        mylist = list(zip(position, speed))
        mylist.sort(reverse=True)
        stack = []
        for pair in mylist:
            timeToTarget = (target - pair[0]) / pair[1]
            stack.append(timeToTarget)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
