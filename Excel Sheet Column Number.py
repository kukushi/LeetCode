class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        factor = 1
        for character in reversed(s):
        	result += (ord(character) - 64) * factor
        	factor *= 26
        return result