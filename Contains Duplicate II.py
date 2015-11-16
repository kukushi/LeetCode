class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        length = len(nums)
        pre = None
        for i in sorted_nums:
            if i == pre:
                pre_index = None
                for it in range(length):
                    j = nums[it]
                    if j == i:
                        if pre_index is not None:
                            if it - pre_index <= k:
                                return True
                        pre_index = it

            pre = i
        return False