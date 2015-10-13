class Solution(object):
    def binary_search(self, nums, start_index, end_index, target):
        middle = (start_index + end_index) >> 1
        number = nums[middle]

        if nums[start_index] == target:
            return start_index
        elif nums[end_index] == target:
            return end_index
        elif number == target:
            return middle

        if (start_index == middle - 1 and end_index == middle + 1) or (end_index - start_index == 1):
            return -1

        if number > target:
            return self.binary_search(nums, start_index, middle, target)
        else:
            return self.binary_search(nums, middle, end_index, target)

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        last_number = sorted_nums[-1]
        index = 0
        length = len(sorted_nums) - 1
        for number in sorted_nums:
            index += 1
            if number + last_number < target:
                pass
            else:
                number_to_find = target - number
                matched_index = self.binary_search(sorted_nums, index, length, number_to_find)
                if matched_index != -1:
                    lv = sorted_nums[index - 1]
                    rv = sorted_nums[matched_index]
                    if lv != rv:
                        index1 = nums.index(lv) + 1
                        index2 = nums.index(rv) + 1
                        return [min(index1, index2), max(index1, index2)]
                    else:
                        result = []
                        index = 1
                        for number in nums:
                            if number == lv:
                                result.append(index)
                            index += 1
                        return result