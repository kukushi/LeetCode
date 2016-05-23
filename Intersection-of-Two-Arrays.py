class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = dict()
        result = []

        for i in nums1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in nums2:
            if i in count:
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
                result.append(i)
        return result


print(Solution().intersect([1,2, 2, 1], [2, 2]))