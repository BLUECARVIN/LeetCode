class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0 # record 0's number

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i - zeros] = nums[i]
        
        for i in range(zeros):
            nums[- (1 + i)] = 0
# ----------- 152ms, 14.9MB ---------- #