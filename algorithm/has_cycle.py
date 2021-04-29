class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head):
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ListNode(3)
    ln1.next = ln2
    ln2.next = ln1
    res = Solution().has_cycle(ln1)
    print(res)
