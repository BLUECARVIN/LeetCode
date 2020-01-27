class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    p = stack.pop()
                    if i == '}' and p != '{':
                        return False
                    elif i == ']' and p != '[':
                        return False
                    elif i == ')' and p != '(':
                        return False
        if len(stack) != 0:
            return False
        return True