# Last updated: 7/27/2026, 2:05:57 PM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        word = 0
4        started = False
5
6        for i in range(len(s) - 1, -1, -1):
7            if s[i] != ' ':
8                word += 1
9                started = True
10            elif started:
11                break
12
13        return word
14