# Last updated: 7/20/2026, 1:37:27 PM
class Solution:
    def minMaxDifference(self, num: int) -> int:

        lowValue, highValue = str(num), str(num)

        for i in highValue:
            if i != "9":
                highValue = highValue.replace(i,'9')
                break
            
        for i in lowValue:
            if i != "0":
                lowValue = lowValue.replace(i,'0')
                break

        return ((int(highValue)) - (int(lowValue)))
                
            
        