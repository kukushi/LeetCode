class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty() == False:
            del self.list[0]

    def peek(self):
        """
        :rtype: int
        """
        if  self.empty() == False:
            return self.list[0]
        return None

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.list) == 0
