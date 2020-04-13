class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        number = str(n)
        s = 0
        m = 1
        for i in number:
            s += int(i)
            m *= int(i)
        return m - s