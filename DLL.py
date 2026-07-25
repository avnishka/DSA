class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


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

    def insertAtPos(self, head, p, x):
        # Code Here
        new = Node(x)
        current = head
        count = 0
        while current and count < p:
            current = current.next
            count += 1
        if current is None:
            return head
        new.next = current.next
        new.prev = current
        if current.next:
            current.next.prev = new
        current.next = new
        return head

    def deleteAtPos(self, head, x):
        if not head:
            return
        current = head
        count = 1
        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head
        while current:
            if count == x:
                break
            current = current.next
            count += 1
        if current.next:
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            current.prev.next = None
        return head


def dll_to_list(head):
    out = []
    while head:
        out.append(head.data)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()

    head = sol.createDLL([1, 2, 3, 4, 5])
    print("createDLL:        ", dll_to_list(head))

    head = sol.insertAtPos(head, 2, 99)
    print("insertAtPos @2:   ", dll_to_list(head))

    head = sol.deleteAtPos(head, 4)
    print("deleteAtPos @4:   ", dll_to_list(head))
