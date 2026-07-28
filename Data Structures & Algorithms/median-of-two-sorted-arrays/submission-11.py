class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # partition where half the nums are on the left, and half on the right
        # can derive median if all the vals on the left are less than all values on the right
        # handle odd and even cases
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = len(nums1) + len(nums2)
        half = total // 2

        # binary search the smaller array and the i is the partitions
        left = 0
        right = len(nums1)
        while left <= right:
            partitionA = (right + left) // 2
            partitionB = half - partitionA

            # extract values around partition to validate the current window
            aLeft = nums1[partitionA-1] if (partitionA-1) >= 0 else float('-inf')
            aRight = nums1[partitionA] if partitionA < len(nums1) else float('inf')
            
            bLeft = nums2[partitionB-1] if (partitionB-1) >= 0 else float('-inf')
            bRight = nums2[partitionB] if partitionB < len(nums2) else float('inf')

            # valid window
            if aLeft <= bRight and bLeft <= aRight:
                # odd case
                if total % 2:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = partitionA -1
            else:
                left = partitionA + 1
        
        return 0