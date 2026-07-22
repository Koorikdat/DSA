# Last updated: 7/22/2026, 2:56:33 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3
4        initial = str(x)
5        reverse = ''
6
7        for i in range(len(initial) -1, -1, -1):
8            reverse += initial[i]
9        
10        return initial == reverse
11
12