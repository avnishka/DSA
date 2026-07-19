"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""


class Solution:
    def lengthOfLoop(self, head):
        # code here
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0

    def lengthOfLoop(self, head):
        # code here
        temp = head
        travel = 0
        my_dict = dict()
        while temp:
            if temp in my_dict:
                return travel - my_dict[temp]
            my_dict[temp] = travel
            travel += 1
            temp = temp.next
        return 0
