# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        if length==n:
            head=head.next
            return head
        remove=length-n-1
        count=0
        temp=head
        while count < remove:
            count+=1
            temp=temp.next
        temp.next=temp.next.next   
        return head