class Solution(object):
	def binarySearch(self, lv, rv, target):
		lv_product = lv * lv
		rv_product = rv * rv
		if lv_product == target:
			return lv
		if rv_product == target:
			return rv

		if lv == rv or (rv - lv == 1):
			return lv

		half_product = (lv + rv) // 2
		if target > half_product * half_product:
			return self.binarySearch(half_product, rv, target)
		return self.binarySearch(lv, half_product, target)
				
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		return self.binarySearch(0, x, x)