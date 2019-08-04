class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(numRows - 2):
            sub_ans = [1]
            for j in range(len(ans[i + 1]) - 1):
                sub_ans.append(ans[i+1][j+1] + ans[i+1][j])
            sub_ans.append(1)
            ans.append(sub_ans)
        return ans
# ---------- 44ms, 13.8MB ---------- #