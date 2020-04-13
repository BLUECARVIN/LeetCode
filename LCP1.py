class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        ans = 0
        for i, j in zip(guess, answer):
            if i == j:
                ans += 1
        return ans