class Solution(object):
    def binarySearch(self, list, target):
        lo = 0
        hi = len(list) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            item = list[mid]
            if item == target:
                return mid
            if target > item:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for list in matrix:
            if list[0] > target:
                return False
            else:
                result = self.binarySearch(list, target)
                if result != -1:
                    return True
        return False
