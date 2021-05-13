# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type: headA, headB: ListNode
#         :rtype: ListNode
#         """
#         p1 = headA
#         p2 = headB
#         while(p1 != p2):
#             p1 = headB if p1 is None else p1.next
#             p2 = headA if p2 is None else p2.next
#         return p1


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def get_intersect_node(self, list_a, list_b):
        head_a = list_a
        head_b = list_b
        len_a, len_b = 0, 0
        while head_a:
            head_a = head_a.next
            len_a += 1
        while head_b:
            head_b = head_b.next
            len_b += 1
        head_a = list_a
        head_b = list_b
        if len_a > len_b:
            for i in range(len_a - len_b):
                head_a = head_a.next
        elif len_b > len_a:
            for i in range(len_b - len_a):
                head_b = head_b.next
        while head_a != head_b:
            head_a = head_a.next
            head_b = head_b.next
        return head_a.val


if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ListNode(3)
    ln3 = ListNode(4)
    ln1.next = ln3
    ln2.next = ln3
    s = Solution()
    print(s.get_intersect_node(ln1, ln2))

