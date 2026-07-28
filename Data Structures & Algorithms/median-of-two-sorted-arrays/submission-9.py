class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total = len(nums1) + len(nums2)
        half = total // 2

        left, right = 0, len(nums1)

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = half - partitionA

            aLeft = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            aRight = nums1[partitionA] if partitionA < len(nums1) else float("inf")

            bLeft = nums2[partitionB - 1] if partitionB > 0 else float("-inf")
            bRight = nums2[partitionB] if partitionB < len(nums2) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)

                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2

            if aLeft > bRight:
                right = partitionA - 1
            else:
                left = partitionA + 1
        
        return 0