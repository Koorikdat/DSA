# Last updated: 7/17/2026, 11:57:54 AM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) == len(goal):
            return goal in s+s
        else:
            return False


        