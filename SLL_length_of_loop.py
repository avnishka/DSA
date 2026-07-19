class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def lengthOfLoop(self, head):
        # code here
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0

    def lengthOfLoop_hashmap(self, head):
        # code here
        temp = head
        travel = 0
        my_dict = dict()
        while temp:
            if temp in my_dict:
                return travel - my_dict[temp]
            my_dict[temp] = travel
            travel += 1
            temp = temp.next
        return 0


def build_loop(arr, loop_index):
    if not arr:
        return None
    nodes = [Node(v) for v in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if 0 <= loop_index < len(nodes):
        nodes[-1].next = nodes[loop_index]
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()

    cases = [
        ([1, 2, 3, 4, 5], 2, 3),
        ([1, 2, 3, 4, 5, 6], 1, 5),
        ([1, 2, 3, 4], -1, 0),
        ([1], 0, 1),
    ]

    for arr, idx, expected in cases:
        head_floyd = build_loop(arr, idx)
        head_hash = build_loop(arr, idx)
        print(f"{arr}, loop at {idx} -> "
              f"floyd={sol.lengthOfLoop(head_floyd)}, "
              f"hashmap={sol.lengthOfLoop_hashmap(head_hash)}, "
              f"expected={expected}")
