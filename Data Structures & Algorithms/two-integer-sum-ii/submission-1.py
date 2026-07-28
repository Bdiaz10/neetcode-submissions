class Solution:
    # returns index if found, else - 1
    def binarySearch(self, nums: list[int], left, right, target) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate list, calculate the needed diff
        for i in range(len(numbers)):
            diff = target - numbers[i]
            searchResult = self.binarySearch(numbers, i, len(numbers)-1, diff)
            if searchResult != -1:
                return [i+1, searchResult+1]

        return [-1,-1]

        # binary search the second half