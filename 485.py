class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        m = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                m += 1
            else:
                if m > ans:
                    ans = m
                m = 0
        if m > ans:
            ans = m
        return ans

# ----------- 500ms, 14.1MB ---------- #