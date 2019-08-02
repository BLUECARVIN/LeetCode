class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        for i in range(len(A)):
            temp = [k for k in A[i][::-1]]
            B.append([1 - l for l in temp])
        return B

# ------------ 120ms, 13.9MB ---------- #
