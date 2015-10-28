class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_count = {}
        for char in s:
        	if char in char_count.keys():
        		char_count[char] += 1
        	else:
        		char_count[char] = 1

        for char in t:
        	if char in char_count.keys():
        		char_count[char] -= 1
        		if char_count[char] == 0:
        			del char_count[char]
        	else:
        		return False
        return len(char_count) == 0