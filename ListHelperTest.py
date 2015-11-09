import os
import sys

scriptpath = "./ListHelper.py"
sys.path.append(os.path.abspath(scriptpath))


import ListHelper
import unittest

class TestAddNumbersMethod(unittest.TestCase):

    def test_singleItemArray(self):
        node = ListHelper.ListNode(1)
        list_helper = ListHelper.ListHelper()
        transfered_list = list_helper.ListNodeFromList([1])
        self.assertEqual(transfered_list, node)
        return

    def test_multipleItemArray(self):
        list_helper = ListHelper.ListHelper()
        node = ListHelper.ListNode(1)
        node.next = ListHelper.ListNode(2)
        transfered_list = list_helper.ListNodeFromList([1, 2])
        self.assertEqual(transfered_list, node)
        return

if  __name__ == '__main__':
    unittest.main()
