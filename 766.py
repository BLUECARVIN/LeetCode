class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 1 or n == 1:
            return True
        
        # validate the numbers along column
        for i in range(m):
            x = i
            y = 0
            t = matrix[x][y]
            while x < m and y < n:
                if matrix[x][y] != t:
                    return False
                x += 1
                y += 1
        
        # validate the numbers along raw
        for i in range(1, n):
            x = 0
            y = i
            t = matrix[x][y]
            while x < m and y < n:
                if matrix[x][y] != t:
                    return False
                x += 1
                y += 1
                
        return True

# ---------- 128ms, 13.9MB ---------- #