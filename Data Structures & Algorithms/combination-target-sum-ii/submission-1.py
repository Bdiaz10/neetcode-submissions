class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, currentPath, currentSum):
            if currentSum == target:
                res.append(currentPath.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if currentSum + candidates[i] > target:
                    break

                currentPath.append(candidates[i])
                dfs(i+1, currentPath, currentSum + candidates[i])
                currentPath.pop()
        
        dfs(0, [], 0)
        return res

