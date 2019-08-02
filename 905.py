class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        
        odd.sort(reverse=True)
        even.sort()
        for i in range(len(odd)):
            even.append(odd[i])
    
        return even
# ---------- 136ms, 14.4MB ---------- #