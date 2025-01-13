class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                nums[index] = nums[i]
                index += 1
                visited.add(nums[i])
        return index
