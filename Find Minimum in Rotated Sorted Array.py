class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        num.sort()
        return num[0]