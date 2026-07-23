# Last updated: 7/23/2026, 10:53:25 AM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3
4        if x == None or x == 0:
5            return 0
6        elif x == 1:
7            return 1
8
9
10        i = 0
11        
12        while i <= x:
13            sum = i * i
14            if sum > x:
15                return i-1
16            else:
17                i += 1