# Last updated: 8/6/2026, 11:15:29 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        haylength = len(haystack)
        needlength = len(needle)

        if needlength == 0:
            return 0

        if haylength < needlength:
            return -1

        for i in range(haylength - needlength + 1):
            match = True

            for j in range(needlength):
                if haystack[i + j] != needle[j]:
                    match = False
                    break

            if match:
                return i

        return -1
