"""
this file contains the stack class definition
"""


class Item:
    """
    this is a docstring
    """
    def __init__(self,data="",next=None):
        self.data = data
        self.next = next


class Stack:
    """
    this is a docstring
    """
    def __init__(self):
        """
        this is a docstring
        """
        self.head = None
    
    def push(self,char):
        """
        this is a docstring
        """
        item = Item(char)
        item.next = self.head
        self.head = item

    def pop(self):
        """
        this is a docstring
        """
        if self.head == None:
            raise IndexError
        item = self.head
        self.head = self.head.next
        return item.data

    def top(self):
        """
        this is a docstring
        """
        if self.head:
            return self.head.data
        raise IndexError

    def size(self):
        """
        this is a docstring
        """
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def clear(self):
        """
        this is a docstring
        """
        self.head = None
