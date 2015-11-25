class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        len_sum = len1 + len2
        it1 = 0
        it2 = 0
        count = 0
        selected = None
        pre = None

        while  it1 < len1 and it2 < len2:
        	item1 = nums1[it1]
        	item2 = nums2[it2]
        	if item1 < item2:
        		selected = item1
        		it1 += 1
        	else:
        		selected = item2
        		it2 += 1

        	if len_sum % 2 == 1:
        		if count == len_sum // 2:
        			return selected
        	elif count == len_sum // 2 - 1:
        		pre = selected
        	elif pre != None:
        		return float(pre + selected) / 2

        	count += 1

        it = it1 if it2 == len2 else it2
        nums = nums1 if it2 == len2 else nums2
        len3 = len2 if it2 == len2 else len1
        len4 = len1 if it2 == len2 else len2

        if len_sum % 2 == 1:
        	return nums[(len4 - len3) // 2]
        elif pre is not None:
        	return float(pre + nums[it]) / 2
        else:
        	return float(nums[(len4 - len3) // 2 - 1] + nums[(len4 - len3) // 2]) / 2

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
print(Solution().findMedianSortedArrays([1, 2], [3, 4, 5, 6]))
print(Solution().findMedianSortedArrays([0], [1, 2, 3, 4]))
print(Solution().findMedianSortedArrays([0, 1], [1, 2, 3, 4]))
print(Solution().findMedianSortedArrays([0, 1], [1, 2, 3, 4, 9, 9, 9, 9, 9, 9, 9]))
print(Solution().findMedianSortedArrays([], [1, 2, 4]))
print(Solution().findMedianSortedArrays([3, 4], []))
print(Solution().findMedianSortedArrays([], [2, 3]))