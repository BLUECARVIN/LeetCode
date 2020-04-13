class Solution:
    def printNumbers(self, n: int) -> List[int]:
        length = int(pow(10, n)) - 1
        ans = [i+1 for i in range(length)]
        return ans