class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {} # use a dict record numbers' times
        
        l = len(nums)
        l_t = int(l/2)
        
        for i in range(l):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        
        for i in dict:
            if dict[i] > l_t:
                ans = i
                break
        
        return ans

# ---------- 260ms,15.2MB ---------- #