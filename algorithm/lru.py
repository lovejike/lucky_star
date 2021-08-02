from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity  # cache的容量
        self.visited = OrderedDict()  # python内置的OrderDict具备排序的功能

    def get(self, key: int):
        if key not in self.visited:
            return -1
        self.visited.move_to_end(key)  # 最近访问的放到链表最后，维护好顺序
        return self.visited[key]

    def put(self, key: int, value: int):
        if key not in self.visited and len(self.visited) == self.capacity:
            # last=False时，按照FIFO顺序弹出键值对
            # 因为我们将最近访问的放到最后，所以最远访问的就是最前的，也就是最first的，故要用FIFO顺序
            self.visited.popitem(last=False)
            self.visited[key] = value
            self.visited.move_to_end(key)  # 最近访问的放到链表最后，维护好顺序

# delete duplicate from list
def removeDuplicates(self, nums):
    n = len(nums)

    if n == 0:
        return 0

    slow, fast = 0, 1

    while fast < n:
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

        fast += 1

    return slow + 1


# delete duplicate from listnode
def delete_duplicates(head):
    if not head:
        return head

    slow, fast = head, head.next

    while fast:
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next

        fast = fast.next

    # 断开与后面重复元素的连接
    slow.next = None
    return head


# 中心扩展算法
class Solution:
    def longestPalindrome(self, s: str):
        # 用n来装字符串长度，res来装答案
        n = len(s)
        res = str()
        # 字符串长度小于2，就返回本身
        if n < 2: return s
        for i in range(n - 1):
            # oddstr是以i为中心的最长回文子串
            oddstr = self.centerExtend(s, i, i)
            # evenstr是以i和i+1为中心的最长回文子串
            evenstr = self.centerExtend(s, i, i + 1)
            temp = oddstr if len(oddstr) > len(evenstr) else evenstr
            if len(temp) > len(res): res = temp

        return res

    def centerExtend(self, s: str, left, right) -> str:

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 这里要注意，跳出while循环时，恰好s[left] != s[right]
        return s[left + 1:right]