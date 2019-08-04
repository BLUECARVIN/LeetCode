class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: (x % 2 != 0))
        b = []
        for i in range(int(len(A) / 2)):
            b.append(A[i])
            b.append(A[-(1+i)])
        return b
# ---------- 320ms, 15.9MB ---------- #

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        A.sort()
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans
# ---------- 320ms, 16.1MB ---------- #