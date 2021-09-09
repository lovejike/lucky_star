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

    # 二进制中1的个数
    def numsof1(self, n):
        count = 0
        while n&0xffffffff !=0:
            count += 1
            n = n & (n-1)
        return count

    # 返回只出现一次的数字
    def find_nums_appear_one(self, array):
        if not array:
            return
        dict = {}
        for i in array:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        # print(dict)
        res = []
        for i in dict:
            if dict[i] == 1:
                res.append(i)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.numsof1(7))
    array = [2,3,4,4]
    print(s.find_nums_appear_one(array))