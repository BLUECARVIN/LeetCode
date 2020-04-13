class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        h = [0] * 58
        ans = 0
        for i in J:
            h[ord(i) - 65] = 1
        for i in S:
            if  h[ord(i) - 65] == 1:
                ans += 1
        return ans