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
        while temp and temp.next:
            if count==remove:
                temp.next=temp.next.next
                break
            count+=1
            temp=temp.next
            
        return head