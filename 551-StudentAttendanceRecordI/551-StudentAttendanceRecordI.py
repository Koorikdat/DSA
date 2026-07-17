# Last updated: 7/17/2026, 11:57:57 AM
class Solution:
    def checkRecord(self, s: str) -> bool:

        counterA = 0
        linkL = 0

        for c in s:
            
            if c == 'A':
                counterA += 1

            if c == 'L':
                linkL += 1

            if c != 'L' and linkL < 3:
                linkL = 0

        if counterA < 2 and linkL < 3:
            return True      
        else:
            return False


        

        



        print(myDict)