from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new = []
        while current:
            new.append(current.val)
            current = current.next
        current = head
        while current:
            value = new.pop()
            current.val = value
            current = current.next
        return head

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            temp = head
            while temp:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            head = prev
            return prev


def list_to_nodes(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def nodes_to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    head1 = list_to_nodes([1, 2, 3, 4, 5])
    print("reverseList:", nodes_to_list(sol.reverseList(head1)))
    head2 = list_to_nodes([1, 2, 3, 4, 5])
    print("reverse:    ", nodes_to_list(sol.reverse(head2)))
