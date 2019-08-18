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

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        s = 0
        
        for i in range(length + 1):
            s += i
        
        for i in range(length):
            s -= nums[i]
        return s
# ---------- 208ms, 15.2MB ---------- #
