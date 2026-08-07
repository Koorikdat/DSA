# Last updated: 8/6/2026, 11:15:26 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = 0
        started = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                word += 1
                started = True
            elif started:
                break

        return word
