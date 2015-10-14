
class Solution(object):
    def longestPrefix(self, lv, rv):
        str = ""
        length = min(len(lv), len(rv))
        for i in range(0, length):
            if lv[i] == rv[i]:
                str = str + lv[i]
            else:
                return str
        return str
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        strs = sorted(strs, key=lambda word: [len(str) for str in word])
        lcp = strs[0]

        is_first = True
        for str in strs:
            if is_first:
                is_first = False
                pass
            else:
                lcp = self.longestPrefix(lcp, str)

        return lcp

print(Solution().longestCommonPrefix(["aca", "cba"]))
        