class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find R's position
        m = 0   # record the line of R
        n = 0   # record the column of R
        # B = []
        # p = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    m = i
                    n = j
                # elif board[i][j] == 'B':
                #     B.append([i, j])
                # elif board[i][j] == 'p':
                #     p.append([i, j])
        
        line = board[m]
        column = []
        for i in range(len(board)):
            column.append(board[i][n])
        
        ans = 0
        ans += self.find_num(line, n)
        ans += self.find_num(column, m)
        
        return ans
    
    # find how much p can be reached in an array
    def find_num(self, arr, m):
        ans = 0
        for i in range(m+1, len(arr)):
            if arr[i] == 'p':
                ans += 1
                break
            elif arr[i] == 'B':
                break
        for i in range(m-1, -1, -1):
            if arr[i] == 'p':
                ans += 1
                break
            elif arr[i] == 'B':
                break
        return ans

# ---------- 44ms, 14MB ---------- #