from linked_list_intro import SinglyLinkedList


class Solution:
    def getCount(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count


def main():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sol = Solution()
    print(sol.getCount(sll.head))


if __name__ == "__main__":
    main()
