class Solution(object):
	def binarySearch(self, lv, rv, target):
		while lv <= rv:
			mid = int(lv + (rv - lv) // 2)
			if mid * mid == target:
				return mid
			elif mid * mid < target:
				lv = mid + 1
			else:
				rv = mid - 1
		return rv
				
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		return int(self.binarySearch(0, x, x))