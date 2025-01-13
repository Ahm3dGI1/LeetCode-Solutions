class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        res = [[]]

        for n in nums1:
            if n not in nums2:
                res[0].append(n)
            else:
                nums2.remove(n)

        res.append(list(nums2))

        return res
