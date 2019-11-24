class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        label = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in label:
                ans = [label[target-nums[i]], i]
            else:
                label[nums[i]] = i
        return ans
# ----------- 76ms, 15.7MB ---------- #

# WHY CANNOT TO SUBMMIT