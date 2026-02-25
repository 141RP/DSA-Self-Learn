## Problem: Count the Number of Nodes in a Linked List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def countNodes(head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count


def run_tests():
    print("Running Linked List Count Tests...\n")

    # Test 1: Empty list
    head = None
    print("Test 1 (Empty list):",
          "PASS" if ListNode.countNodes(head) == 0 else "FAIL")

    # Test 2: Single node
    head = ListNode(10)
    print("Test 2 (Single node):",
          "PASS" if ListNode.countNodes(head) == 1 else "FAIL")

    # Test 3: Two nodes
    head = ListNode(1)
    head.next = ListNode(2)
    print("Test 3 (Two nodes):",
          "PASS" if ListNode.countNodes(head) == 2 else "FAIL")

    # Test 4: Multiple nodes
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print("Test 4 (Four nodes):",
          "PASS" if ListNode.countNodes(head) == 4 else "FAIL")

    # Test 5: Large list (1000 nodes)
    head = ListNode(1)
    current = head
    for i in range(2, 1001):
        current.next = ListNode(i)
        current = current.next

    print("Test 5 (1000 nodes):",
          "PASS" if ListNode.countNodes(head) == 1000 else "FAIL")

run_tests()