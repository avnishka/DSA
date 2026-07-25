# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        count=0
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        if n==length:
            head=head.next
            return head      
        while count < n:
            count+=1
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head