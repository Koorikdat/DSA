# Last updated: 7/17/2026, 11:57:46 AM
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        counter = 0
        length = len(words)

        for i in range (0, length):

            for j in range(i + 1, length):

                if words[j].startswith(words[i]) and words[j].endswith(words[i]):

                    counter += 1

        return counter




             


