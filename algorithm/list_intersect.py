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


if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(4)
    ln1.next = ln2
    ln3.next = ln4
    s = Solution()
    print(s.get_intersect_node(ln1, ln3))

