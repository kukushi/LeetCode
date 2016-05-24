class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = dict()
        result = []

        for i in nums1:
            count[i] = 1
        for i in nums2:
            if i in count:
                del count[i]
                result.append(i)
        return result


print(Solution().intersection([1,2, 2, 1], [2, 2]))