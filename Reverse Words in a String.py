class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        string_list = list()

        temp_str = ""
        for i in s:
            if i == " ":
               if len(temp_str):
                   string_list.append(temp_str)
                   temp_str = ""
            else:
                temp_str += i

        if len(temp_str):
            string_list.append(temp_str)

        string_list.reverse()
        return " ".join(string_list)