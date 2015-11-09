import os
import sys

scriptpath = "./ListHelper.py"
sys.path.append(os.path.abspath(scriptpath))

from ListHelper import ListHelper
from ListHelper import ListNode
import unittest

class TestAddNumbersMethod(unittest.TestCase):

    def test_singleItemArray(self):
        node = ListNode(1)
        transfered_list = ListHelper.listNodeFromList([1])
        self.assertEqual(transfered_list, node)
        return

    def test_multipleItemArray(self):
        node = ListNode(1)
        node.next = ListNode(2)
        transfered_list = ListHelper.listNodeFromList([1, 2])
        self.assertEqual(transfered_list, node)
        return

if  __name__ == '__main__':
    unittest.main()
