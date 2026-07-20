# Last updated: 7/20/2026, 1:37:42 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        
    
        myDict = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0

        for x in range(0, len(s)):

            if x < len(s) - 1 and myDict[s[x]] < myDict[s[x+1]]:
                result -= myDict[s[x]]
            
            else:
                s[x] in myDict
                result = result + myDict.get(s[x])

        return result
