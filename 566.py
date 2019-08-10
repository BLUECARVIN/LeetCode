class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        
        print(m, n)
        if m*n != r*c:
            return nums
        
        ans = []
        temp = []
        k = c
        
        for i in range(m):
            for j in range(n):
                temp.append(nums[i][j])
                k -= 1
                if k == 0:
                    ans.append(temp)
                    temp = []
                    k = c
        return ans
# ---------- 104ms, 12.6MB ---------- #