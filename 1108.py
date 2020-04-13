class Solution:
    def defangIPaddr(self, address: str) -> str:
        str_list = address.split('.')
        ans = ''
        for i in range(len(str_list) - 1):
            ans = ans + str_list[i] + '[.]'
        ans += str_list[-1]
        return ans 