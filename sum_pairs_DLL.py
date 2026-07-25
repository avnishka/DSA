# Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def givenSumPairs(self, head, target):
        # code here
        answer = []
        slow = head
        fast = head
        while fast.next:
            fast = fast.next
        while slow != fast and fast.next != slow:
            sums = slow.data + fast.data
            if sums == target:
                answer.append([slow.data, fast.data])
                slow = slow.next
                fast = fast.prev
            elif sums > target:
                fast = fast.prev
            else:
                slow = slow.next
        return answer


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

    head = build_dll([1, 2, 4, 5, 6, 8, 9])
    target = 10
    print(f"dll:    {dll_to_list(head)}")
    print(f"target: {target}")
    print("pairs: ", sol.givenSumPairs(head, target))
