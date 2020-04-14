class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        index = []
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                j = stack.pop()
            if len(stack) == 0:
                index.append(j)
                index.append(i)
        S = list(S)
        cnt = 0
        for i in index:
            S.pop(i - cnt)
            cnt += 1
        return "".join(S)