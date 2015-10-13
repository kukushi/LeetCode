class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nums = []

        if x < 0:
            return False

        while x != 0:
            nums.append(x % 10)
            x = x // 10

        length = len(nums)
        for i in range(0, length // 2):
            if nums[i] != nums[length - 1 - i]:
                return False

        return  True


print(Solution().isPalindrome(-2147483648))