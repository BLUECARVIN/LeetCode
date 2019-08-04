class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        table = [101 for i in range(26)]
        
        for i in range(len(A)):
            sub_table = [0 for i in range(26)]
            for j in range(len(A[i])):
                sub_table[ord(A[i][j]) - 97] += 1
            for j in range(26):
                table[j] = min(table[j], sub_table[j])
        
        ans = []
        for i in range(26):
            if table[i] != 101:
                for j in range(table[i]):
                    ans.append(chr(97 + i))
        
        return ans
# ---------- 88ms, 13.9MB ---------- #