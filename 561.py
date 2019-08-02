class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = sum([i for i in nums[::2]])
        return ans
# ---------- 420ms, 16.4MB ---------- #