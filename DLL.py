"""class Node:
def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
"""


class Solution:
    def createDLL(self, arr):
        # code here
        if not arr:
            return None

        head = Node(arr[0])
        prev = head

        for i in range(1, len(arr)):
            new = Node(arr[i])
            prev.next = new
            new.prev = prev
            prev = new
        return head
