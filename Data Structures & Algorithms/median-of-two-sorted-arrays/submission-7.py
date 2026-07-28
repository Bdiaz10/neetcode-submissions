class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # create partitions where the left side and right side are equal to half the total
        # validate windows where the left side is less than the right side
        # binary search the smaller array, caluclating the second partition automatically
        # move the binary search pointers to make the left side less than the right side
        # calculate the medium by handling odd and even totals
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = len(nums1) + len(nums2)
        half = total // 2

        left = 0
        right = len(nums1)-1
        while True:
            partitionA = (left + right) // 2
            partitionB = half - partitionA - 2

            aLeft = nums1[partitionA] if partitionA >= 0 else float('-inf')
            aRight = nums1[partitionA + 1] if (partitionA+1) < len(nums1) else float('inf')

            bLeft = nums2[partitionB] if partitionB >= 0 else float('-inf')
            bRight = nums2[partitionB + 1] if (partitionB+1) < len(nums2) else float('inf')

            # validate partitions
            if aLeft <= bRight and bLeft <= aRight:
                if total % 2: # odd case
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = partitionA -1
            else:
                left = partitionA + 1
        
        return 0