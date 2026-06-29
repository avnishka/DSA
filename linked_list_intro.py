class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traversal(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next

    def insert_at(self, val, pos):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current and count < pos:
                prev = current
                current = current.next
                count += 1
            prev.next = new_node
            new_node.next = current


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(node1)
    print(node1.val)
    print(node1.next)
    print(node1.next.val)
    print(node1.next.next)
    print(node1.next.next.val)

    sll = SinglyLinkedList()
    sll.append(8)
    sll.append(9)
    sll.append(10)
    sll.traversal()
