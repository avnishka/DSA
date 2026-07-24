# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        new=[]
        temp=head
        while temp:
            new.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                temp = None
        temp=head
        temp=temp.next
        while temp:
            new.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                temp = None
        temp=head
        for i in range(len(new)):
            temp.val=new[i]
            temp=temp.next
        return head
        

