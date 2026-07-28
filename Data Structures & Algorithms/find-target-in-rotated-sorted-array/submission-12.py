class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot index
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        def binarySearch(left, right) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return -1
        pivot = left
        print(pivot)

        res = binarySearch(0, pivot-1)
        if res != -1:
            return res
        return binarySearch(pivot, len(nums)-1)