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


class Solution:
    # 删除链表倒数第n个节点
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

    # 判断两个单链表交点
    def get_intersect_node(self, headA, headB) :
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        if nodeA:
            return True
        else:
            return False

    # 判断链表是否有环
    def has_cycle(self, head):
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False

    # 判断是否回文链表
    def is_palindrome(self, head):
        if not head:
            return
        # 翻转前半部分
        fast = cur = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        if fast:
            cur = cur.next
        while cur and cur.val == prev.val:
            cur, prev = cur.next, prev.next
        return not prev

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

