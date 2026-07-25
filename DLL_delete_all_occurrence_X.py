class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        current = head
        while current:
            if current.data == x:
                if current.prev:
                    current.prev.next = current.next
                else:
                    head = head.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
            current = current.next
        return head


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

    arr = [2, 3, 2, 4, 2, 5, 2]
    x = 2
    head = build_dll(arr)
    print(f"original:            {dll_to_list(head)}")
    head = sol.deleteAllOccurOfX(head, x)
    print(f"after deleting {x}: {dll_to_list(head)}")

    head2 = build_dll([7, 7, 7, 1, 7])
    print(f"original:            {dll_to_list(head2)}")
    head2 = sol.deleteAllOccurOfX(head2, 7)
    print(f"after deleting 7:   {dll_to_list(head2)}")

    head3 = build_dll([1, 2, 3])
    print(f"no match:            {dll_to_list(sol.deleteAllOccurOfX(head3, 99))}")