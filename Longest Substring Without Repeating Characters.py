class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = dict()
        count = 0
        cutted = False
        result = 1
        last_cutted = 1
        counter = 0
        for char in s:
            count += 1
            if char in cache:
                cutted = True
                result = max(result, counter)
                cached_char = cache[char]
                if cached_char < count - counter:
                    counter += 1
                else:
                    counter = count - cached_char
                last_cutted = count
            else:
                counter += 1
            result = max(result, counter)
            cache[char] = count

        if not cutted:
            return len(s)
        else:
            result = max(result, len(s) - last_cutted + 1)

        return result
