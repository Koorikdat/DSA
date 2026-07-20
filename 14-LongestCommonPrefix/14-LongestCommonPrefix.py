# Last updated: 7/20/2026, 1:37:41 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''
        strs.sort()

        first = strs[0]
        last = strs[-1]
        interval = min(len(first),len(last))
       

        ans = ''

        for i in range(0, interval):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break

        return ans