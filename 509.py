class Solution:
    def fib(self, N: int) -> int:
        memory = {}
        ans = self.fib_cal(N, memory)
        return ans
    
    def fib_cal(self, N, memory):
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        if memory.get(N) != None:
            ans = memory[N]
            return ans
        else:
            ans = self.fib_cal(N-1, memory) + self.fib_cal(N-2, memory)
            memory[N] = ans
            return ans
# ---------- 52ms, 13.9MB ----------- #