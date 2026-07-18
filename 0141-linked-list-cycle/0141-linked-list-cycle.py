# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set=set()
        temp=head
        cycle=False
        while temp:
            if temp in my_set:
                cycle=True
                break
            my_set.add(temp)
            temp=temp.next
        return cycle
        