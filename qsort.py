class Solution:
    def qsort(self, array):
        start = 0
        end = len(array) - 1
        self.dive(array, start, end)
        return array

    def dive(self, array, start, end):
        index = self.divide(array, start, end)

        if index - start > 1:
            self.dive(array, start, index - 1)
        if end - index > 1:
            self.dive(array, index + 1, end)

    def divide(self, array, start, end):
        last = array[end]
        index = start
        for i in range(start, end + 1):
            if array[i] < last:
                array[index], array[i] = array[i], array[index]
                index += 1
        array[index], array[i] = array[i],array[index]
        return index

print(Solution().qsort([1, 3, 5, 67, -1, 0, 0]))