class Solution:
    def quickselect(self, array, k):
        index = -1
        start = 0
        end = len(array)

        while index != k:
            index, value = self.partition(array, start, end)
            if index == k:
                return value
            elif index < k:
                start = index + 1
            else:
                end = index - 1

    def partition(self, array, start, end):
        if start == end:
            return (start, array[start])

        less_index = start
        value = array[end - 1]

        for index in range(start, end):
            if array[index] <= value:
                array[less_index], array[index] = array[index], array[less_index]
                less_index += 1
        return (less_index - 1, value)