class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                res[0] = mid
                res[1] = mid
                break

            elif nums[mid] < target:
                l = mid+1

            else:
                r = mid-1

        if res == [-1, -1]:
            return res

        l = 0
        r = res[0]

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                res[0] = mid
                r = mid-1

            elif nums[mid] < target:
                l = mid+1

            else:
                r = mid-1

        l = res[1]
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                res[1] = mid
                l = mid+1

            elif nums[mid] < target:
                l = mid+1

            else:
                r = mid-1

        return res
