# 判断是否是回文链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def is_palindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         prev = None
#         fast = cur = head
#         while fast and fast.next:  # 翻转链表的前n/2个结点，prev为翻转后的头结点
#             fast = fast.next.next
#             next_node = cur.next
#             cur.next = prev
#             prev = cur
#             cur = next_node
#             # prev, prev.next, slow = slow, prev, slow.next
#         if fast:  # 结点个数为奇数时，跳过最中间的结点
#             cur = cur.next
#         while cur and cur.val == prev.val:  # 前n/2个结点翻转后，与剩下的结点进行对比
#             prev, cur = prev.next, cur.next
#         return not prev


class Solution:
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
    l3 = ListNode(2)
    l4 = ListNode(1)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    s = Solution()
    print(s.is_palindrome(l1))

