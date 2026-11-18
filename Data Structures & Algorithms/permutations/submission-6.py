class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

            # [1] -> [1,2] -> [1,2,3]
            #     -> [1,3] -> [1,3,2]

# []        # [2] -> [2,1] -> [2,1,3]
            #     -> [2,3] -> [2,3,1]

            # [3] -> [3,1] -> [3,1,2]
            #     -> [3,2] -> [3,2,1]

        # i need to build this tree
        # at a leaf node, add to result

        # root/ starting value is []
        
        # choose an element from nums, add to path
        # remove that number from nums
        result = []
        def backtrack(numbers, currentPerm):
            if len(currentPerm) == len(nums):
                result.append(currentPerm.copy())
                return
            
            for i, n in enumerate(numbers):
                currentPerm.append(n)
                newNums = numbers[:i] + numbers[i+1:]
                backtrack(newNums, currentPerm)
                currentPerm.pop()
        
        backtrack(nums, [])
        return result

        # numbers = [1,2,3]
        # currentPerm = []

        # i = 0
        # currentPerm = [1]
        # newNums = [2,3]
        # backtrack([2,3], [1])
        # currentPerm = []
        # i = 1
        # currentPerm = [2]
        # newNums [1,3]
        # backtrack([1,3], [2])

        # backtrack([2,3], [1])
        # i = 0
        # currentPerm = [1,2]
        # newNums = [3]
        # backtrack([3], [1,2])
        # currentPerm = [1]
        # i = 1
        # currentPerm = [1,3]
        # newNums = [2]
        # backtrack([2], [1,3])
        # currentPerm = [1]
        # i = 2
        # i > len(nums):
        #return

        # backtrack([2], [1,3])
        # currentPerm [1,3,2]
        # newNums = []
        # backtrack([], [1,3,2])
        # base case add to result and return

        # backtrack([3], [1,2])
        # i = 0
        # currentPerm = [1,2,3]
        # newNums = []
        # backtrack([], [1,2,3])
        # currentPerm = [1,2]
        # i = 1
        # i > numbers return

        # backtrack([], [1,2,3])
        # append [1,2,3] to result and return


