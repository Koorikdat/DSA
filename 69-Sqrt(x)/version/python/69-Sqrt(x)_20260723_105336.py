# Last updated: 7/23/2026, 10:53:36 AM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3
4        if x == None or x == 0:
5            return 0
6            
7        elif x == 1:
8            return 1
9
10
11        i = 0
12        
13        while i <= x:
14            sum = i * i
15            if sum > x:
16                return i-1
17            else:
18                i += 1