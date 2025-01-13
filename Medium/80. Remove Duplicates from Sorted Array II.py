class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        check = False
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                check = False
                nums[index] = nums[i]
                index += 1
            elif nums[i] == nums[i-1] and not check:
                check = True
                nums[index] = nums[i]
                index += 1
        return index
