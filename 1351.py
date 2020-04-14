class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] < 0:
                    ans += 1
                else:
                    break
        return ans 