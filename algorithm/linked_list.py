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

# 删除链表倒数第n个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        fast = slow = head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            pre = pre.next
            slow = slow.next
        pre.next = slow.next
        return dummy.next

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

