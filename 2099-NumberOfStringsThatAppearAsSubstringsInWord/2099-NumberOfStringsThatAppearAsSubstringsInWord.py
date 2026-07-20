# Last updated: 7/20/2026, 1:37:28 PM
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        # Loop through each individual pattern string
        for pattern in patterns:
            # Check if the pattern exists as a substring inside word
            if pattern in word:
                count += 1
        return count