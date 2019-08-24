class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True
        
        j = 1
        while j < len(A):
            if A[j] - A[j-1] > 0:
                flag = 1
                break
            if A[j] - A[j-1] < 0:
                flag = 0
                break
            j += 1
        if j == len(A):
            return True
        
        if flag == 1:
            for i in range(j+1, len(A)):
                if A[i] - A[i-1] < 0:
                    return False
        
        if flag == 0:
            for i in range(j+1, len(A)):
                if A[i] - A[i-1] > 0:
                    return False
        
        return True
# ---------- 704ms, 19.7MB ---------- #