class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        array_length = len(nums)
        set_length = len(set(nums))
        return array_length != set_length

print(Solution().containsDuplicate([1,2,3]))