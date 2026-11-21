class Solution:
    def climbStairs(self, n: int) -> int:
        # either take 1 step, or 2 steps
        # 1 way to get to step one: [step]
        # 2 ways to get to step two: [step, step] [jump]

        
        # steps to reach n = steps to reach n-1 + steps to reach n-2
        cache = {
            1: 1,
            2: 2
        }

        def dp(step):
            if step in cache:
                return cache[step]
            cache[step] = dp(step-1) + dp(step-2)
            return cache[step]

        dp(n)
        return cache[n]