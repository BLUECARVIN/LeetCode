class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = -1
        length = len(nums)
        
        
        while i <= length + j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1

        return i

# ----------- 56ms,13.7MB ---------- #