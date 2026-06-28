class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insertAtEnd(self, head, x):
        # code here
        new_node = Node(x)
        if head is None:
            return new_node
        current = head
        while current.next != None:
            current = current.next
        current.next = new_node
        return head

    def printList(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def main(self):
        head = None
        head = self.insertAtEnd(head, 10)
        head = self.insertAtEnd(head, 20)
        head = self.insertAtEnd(head, 30)
        self.printList(head)


if __name__ == "__main__":
    node = Node(None)
    node.main()
