class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hash = [0] * 101
        for i in nums:
            hash[i] += 1
        return [sum(hash[:i]) for i in nums]