class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # create partition where left = half elements and right = half elements
        # all values on the left are smaller than than the values on the right

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        half = (len(nums1) + len(nums2)) // 2

        left = 0
        right = len(nums1)-1
        while True:
            partitionA = (right + left) // 2
            partitionB = half - partitionA - 2

            # partitionA border elements
            aLeft = nums1[partitionA] if partitionA >= 0 else float('-inf')
            aRight = nums1[partitionA + 1] if (partitionA+1) < len(nums1) else float('inf')

            # partitionB border elements
            bLeft = nums2[partitionB] if partitionB >= 0 else float('-inf')
            bRight = nums2[partitionB + 1] if (partitionB+1) < len(nums2) else float('inf')

            # partition is correct
            if aLeft <= bRight and bLeft <= aRight:
                # handle odd case
                if (len(nums1) + len(nums2)) % 2:
                    return min(aRight, bRight)
                # even case
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = partitionA -1
            else:
                left = partitionA + 1
        
        return float('inf')