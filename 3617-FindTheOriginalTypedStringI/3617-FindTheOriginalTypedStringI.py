# Last updated: 7/20/2026, 1:37:26 PM
class Solution:
    def possibleStringCount(self, word: str) -> int:

        counter = 1

        for i in range(0, len(word)):
            if i>0:
                if word[i] == word[i-1]:
                    counter +=1
        return counter