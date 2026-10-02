class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. A median has half the elements to the left, and half the elements to the right
        # 2. All value to the left are <= the median, all values to the right are >= the median
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        left = 0
        right = len(nums1)
        while left <= right:
            partitionA = left + (right - left) // 2
            partitionB = half - partitionA

            aLeft = nums1[partitionA-1] if partitionA > 0 else float('-inf')
            aRight = nums1[partitionA] if partitionA < len(nums1) else float('inf')

            bLeft = nums2[partitionB-1] if partitionB > 0 else float('-inf')
            bRight = nums2[partitionB] if partitionB < len(nums2) else float('inf')


            # we automatically calulated partitionB, 
            #  so we know left and right contain the corrent number of elements

            # we need to make sure all the left elements are less than all the right elements

            # valid window
            if aLeft <= bRight and bLeft <= aRight:
                if total % 2: # odd case
                    # [1, 2, 5] [3, 6]
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aRight < bLeft:
                left = partitionA +1 
            else:
                right = partitionA -1
        
        return 0