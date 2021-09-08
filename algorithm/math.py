class Solution(object):
    # 判断只出现一次的数字
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
    def numsof1(self, n):
        count = 0
        while n&0xffffffff !=0:
            count += 1
            n = n & (n-1)
        return count