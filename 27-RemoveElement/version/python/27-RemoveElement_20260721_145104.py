# Last updated: 7/21/2026, 2:51:04 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3
4        haylength = len(haystack)
5        needlength = len(needle)
6
7        if needlength == 0:
8            return 0
9
10        if haylength < needlength:
11            return -1
12
13        for i in range(haylength - needlength + 1):
14            match = True
15
16            for j in range(needlength):
17                if haystack[i + j] != needle[j]:
18                    match = False
19                    break
20
21            if match:
22                return i
23
24        return -1
25