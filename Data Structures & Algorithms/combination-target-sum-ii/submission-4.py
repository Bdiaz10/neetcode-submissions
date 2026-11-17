class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # contains duplicates
        # can only choose a candidate once

        candidates.sort()
        result = []
        def backtrack(i, currentPath, currentSum):
            if currentSum > target:
                return
            if i >= len(candidates):
                if currentSum == target:
                    result.append(currentPath.copy())
                    return
                return
            
            currentPath.append(candidates[i])
            backtrack(i+1, currentPath, currentSum + candidates[i])

            currentPath.pop()
            curr = candidates[i]
            while i < len(candidates) and candidates[i] == curr:
                i += 1
            backtrack(i, currentPath, currentSum)

        backtrack(0, [], 0)
        return result
                
            