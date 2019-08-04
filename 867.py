class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(c) for c in zip(*A)]

# ---------- 108ms, 14.6MB ----------- #