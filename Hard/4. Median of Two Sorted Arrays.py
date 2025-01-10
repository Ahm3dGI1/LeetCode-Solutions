class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        mid_point = total_len // 2

        i, j = 0, 0
        current, prev = 0, 0

        for _ in range(mid_point + 1):
            prev = current

            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1

        if total_len % 2 == 0:
            return (current + prev) / 2
        else:
            return current
