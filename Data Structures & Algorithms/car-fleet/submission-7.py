class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mylist = [(p, s) for p, s in zip(position, speed)]
        mylist.sort(reverse=True)
        print(mylist)

        stack = []

        for pair in mylist:
            timeToTarget = (target - pair[0]) / pair[1]
            stack.append(timeToTarget)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        print(stack)
        return len(stack)

