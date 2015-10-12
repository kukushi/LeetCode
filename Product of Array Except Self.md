class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 1
        contain_zero = 0

        for number in nums:
            if number == 0:
                contain_zero += 1
            else:
                sum *= number

        numbers = []

        if contain_zero == 0:
            for number in nums:
                numbers.append(sum // number)
        else:
            if contain_zero > 1:
                for number in nums:
                    numbers.append(0)
            else:
                for number in nums:
                    if number == 0:
                        numbers.append(sum)
                    else:
                        numbers.append(0)
                
        return numbers