class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_list = []
        index = 0
        for item in height:
            height_list.append((item, index))
            index += 1
        height_list = sorted(height_list, key=lambda item: item[0])


        length = len(height_list)
        length_it = length - 1
        data_list = []
        max_index = -1
        min_index = 1000000
        while length_it >= 0:
            current_index = height_list[length_it][1]
            max_index = max(max_index, current_index)
            min_index = min(min_index, current_index)
            data_list.insert(0, (max_index, min_index))
            length_it -= 1 

        result = 0
        item_index = 0
        for item in height_list:
            height = item[0]
            index = item[1]
            if item_index + 1 < length:
                max_index = data_list[item_index + 1][0]
                min_index = data_list[item_index + 1][1]
                if min_index < index:
                    result = max(result, height * (index - min_index))
                if max_index > index:
                    result = max(result, height * (max_index - index))
            item_index += 1

        return result