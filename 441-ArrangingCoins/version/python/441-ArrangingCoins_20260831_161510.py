# Last updated: 8/31/2026, 4:15:10 PM
1class Solution:
2    def checkRecord(self, s: str) -> bool:
3
4        ACounter = 0
5        LCounter = 0
6
7        for i in range (0, len(s)):
8
9           
10
11            if s[i] == "A":
12                ACounter += 1
13                LCounter = 0
14            
15            if s[i] == "L":
16                LCounter += 1
17            
18            if s[i] == "P":
19                LCounter = 0
20
21
22
23            if ACounter>1:
24                return False
25            if LCounter==3:
26                return False
27        
28        return True
29 
30
31            
32        