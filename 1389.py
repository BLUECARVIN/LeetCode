class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans = ans[:index[i]] + [nums[i]] + ans[index[i]:]
        return ans