class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverse(self, head):
        if not head:
            return None

        current = head
        while current:
            current.next, current.prev = current.prev, current.next

            if current.prev is None:
                return current

            current = current.prev


def build_dll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    prev = head
    for v in arr[1:]:
        new = Node(v)
        prev.next = new
        new.prev = prev
        prev = new
    return head


def dll_to_list(head):
    out = []
    while head:
        out.append(head.data)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()

    head = build_dll([1, 2, 3, 4, 5])
    print("original:  ", dll_to_list(head))

    rev = sol.reverse(head)
    print("reversed:  ", dll_to_list(rev))

    empty = sol.reverse(None)
    print("empty list:", empty)