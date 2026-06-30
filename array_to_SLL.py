class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def arrayToList(self, arr):
        # code here
        if not arr:
            return None

        head = Node(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = Node(arr[i])
            current = current.next
        return head


arr = [1, 2, 3, 4]
head = Node.arrayToList(arr)
print(head.data, head.next.data, head.next.next.data, head.next.next.next.data)
