class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        total = n+m

        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        l = 0
        r = n-1

        while True:
            i = (l+r)//2
            j = (total//2) - i - 2

            left1 = nums1[i] if i >= 0 else float("-inf")
            right1 = nums1[i+1] if (i+1) < n else float("inf")
            left2 = nums2[j] if j >= 0 else float("-inf")
            right2 = nums2[j+1] if (j+1) < m else float("inf")

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return min(right1, right2)

            if left1 > right2:
                r = i-1
            else:
                l = i+1
