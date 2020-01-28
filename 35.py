class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                p = i
                break
            if i == len(nums) - 1:
                p = len(nums)
        return p
        