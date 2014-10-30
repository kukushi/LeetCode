class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        i = num[0]
        for k in num:
            if k < i:
                return k
            else:
                i = k
        return num[0]