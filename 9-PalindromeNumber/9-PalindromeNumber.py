# Last updated: 7/20/2026, 1:37:43 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        reverse = ''
        s = str(x)

        if x < 0:
            return False
        for i in range(len(s) - 1, -1, -1):
            reverse += s[i]

        if int(reverse) == int(x):
            return True
        else:
            return False 