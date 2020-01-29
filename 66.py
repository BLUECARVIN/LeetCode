class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        length = len(digits)
        answer = [0 for i in range(length+1)]
        for i in range(length):
            t = digits[length - 1 - i] + flag 
            answer[length - i] = t % 10
            if t >= 10:
                flag = 1
            else:
                flag = 0
        answer[0] += flag
        if answer[0] == 0:
            return answer[1:]
        else:
            return answer