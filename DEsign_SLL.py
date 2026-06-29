class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or self.size <= index:
            return -1
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.dummy.next
        self.dummy.next = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        count = 0
        new = ListNode(val)
        current = self.dummy
        while current.next:
            count += 1
            current = current.next
        current.next = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        new = ListNode(val)
        prev = self.dummy

        for _ in range(index):
            prev = prev.next

        new.next = prev.next
        prev.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.dummy

        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1

    # Your MyLinkedList object will be instantiated and called as such:
    # obj = MyLinkedList()
    # param_1 = obj.get(index)
    # obj.addAtHead(val)
    # obj.addAtTail(val)
    # obj.addAtIndex(index,val)
    # obj.deleteAtIndex(index)

    def main(self):
        obj = MyLinkedList()
        obj.addAtHead(1)
        obj.addAtTail(3)
        obj.addAtIndex(1, 2)
        print(obj.get(1))
        obj.deleteAtIndex(1)
        print(obj.get(1))


if __name__ == "__main__":
    MyLinkedList().main()
