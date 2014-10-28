class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProductNoZero(self, A):
        if len(A) > 0:
            sum_result = 1
            negative_count = 0
            product = list()
            for i in A:
                if i < 0:
                    negative_count += 1
                sum_result *= i
                product.append(sum_result)

            if sum_result > 0:
                return sum_result
            else:
                for i in range(len(A)):
                    if A[i] < 0:
                        if i > 0:
                            sum_result = max(product[i - 1], sum_result / A[i] / product[i - 1], sum_result)
                        elif (len(A) > 1):
                            sum_result = max(sum_result, sum_result / A[i])

            return sum_result
        else:
            return 0

    def maxProduct(self, A):
        divided_list = list()
        divided_list.append(list())
        current_list = divided_list[0]
        list_counter = 0
        index = 0

        meetZero = 0
        for i in A:
            if i == 0 and index != 0:
                list_counter += 1
                divided_list.append(list())
                current_list = divided_list[list_counter]
                meetZero = 1
            elif i == 0:
                meetZero = 1
                continue
            else:
                current_list.append(i)
            index += 1

        if meetZero == 0:
            sum = self.maxProductNoZero(divided_list[0])
        else:
            sum = 0
        for i in divided_list:
            sum = max(self.maxProductNoZero(i), sum)
        return sum