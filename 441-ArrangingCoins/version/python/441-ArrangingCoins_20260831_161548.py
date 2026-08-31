# Last updated: 8/31/2026, 4:15:48 PM
1class Solution:
2    def checkRecord(self, s: str) -> bool:
3
4        ACounter = 0
5        LCounter = 0
6
7        for i in range (0, len(s)):           
8
9            if s[i] == "A":
10                ACounter += 1
11                LCounter = 0
12            
13            if s[i] == "L":
14                LCounter += 1
15            
16            if s[i] == "P":
17                LCounter = 0
18
19            if ACounter>1 or LCounter==3:
20                return False
21        
22        return True
23 
24
25            
26        