class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        label = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            label[nums[i]] = 1
        
        for i in range(len(label)):
            if label[i] == 0:
                ans = i
        return ans
# ---------- 216ms, 14.8MB ----------- #
