# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def append(self, origin_list, appended_list, advance):
        origin_list.next = appended_list
        the_advance = advance
        while the_advance != 0:
            plus_result = appended_list.val + the_advance
            appended_list.val = plus_result % 10
            the_advance = plus_result // 10
            if the_advance != 0 and appended_list.next == None:
                appended_list.next = ListNode(0)
            appended_list = appended_list.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        advance = 0
        link_result = None
        link_head = None

        if l1 == None:
            return l2
        elif l2 == None:
            return l1


        while (l1 and l2):
            #
            plus_result = l1.val + l2.val + advance
            advance = plus_result // 10
            link_node = ListNode(plus_result % 10)

            if link_result != None:
                link_result.next = link_node
                link_result = link_result.next
            else:
                link_result = link_node
                link_head = link_node

            #
            l1 = l1.next
            l2 = l2.next


        if l2 != None:
            self.append(link_result, l2, advance)
        elif l1 != None:
            self.append(link_result, l1, advance)
        elif advance != 0:
            link_result.next = ListNode(1)
            
        return link_head