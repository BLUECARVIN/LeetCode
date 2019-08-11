class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        times = len(queries)
        A_len = len(A)
        
        for i in range(times):
            temp = 0
            val = queries[i][0]
            index = queries[i][1]
            
            A[index] += val
            
            for j in range(A_len):
                if A[j] % 2 == 0:
                    temp += A[j]
            
            ans.append(temp)
        
        return ans

# ---------- out of time ---------- #