# 1.链表反转
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def traverse_list(self, head):
        prev = next = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = cur.next
        return prev

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    # while l1:
    #     print(l1.val)
    #     l1 = l1.next
    s = Solution()
    l1 = s.traverse_list(l1)
    while l1:
        print(l1.val)
        l1 = l1.next

