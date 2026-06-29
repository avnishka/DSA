from linked_list_intro import SinglyLinkedList


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def searchKey(self, head, key):
        # Code here
        current = head
        while current:
            if current.val == key:
                return True
            else:
                current = current.next
        return False

    def searchKey_recursive(self, head, key):
        if not head:
            return False
        if head.val == key:
            return True
        return self.searchKey_recursive(head.next, key)

    def main(self):
        sll = SinglyLinkedList()
        sll.append(10)
        sll.append(20)
        sll.append(30)
        print(self.searchKey(sll.head, 20))
        print(self.searchKey_recursive(sll.head, 20))


if __name__ == "__main__":
    solution = Solution()
    solution.main()
