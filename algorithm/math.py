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

    # 第一种: 判断数组中倒数第K大的数
    def find_k_largest1(self, in_list, k):
        in_list.sort()
        return in_list[-k]

    # 第二种: 判断数组中倒数第K大的数
    def find_k_largest2(in_list, k):
        kmax = [float('-inf')] * k
        for i in range(len(in_list)):
            j = 0
            while j < k:
                if in_list[i] > kmax[j]:
                    kmax[j + 1:] = kmax[j:k - 1]
                    kmax[j] = in_list[i]
                    break
                else:
                    j += 1
        return kmax[k - 1]

    # 计算数字的平方根
    def dichotomy_sqrt(x):
        index = -1
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid < x:
                index = mid
                low = mid + 1
            else:
                high = mid - 1

        return index

    # 三角形最大周长
    def largest_perimeter(self, list):
        if not list:
            return 0
        if len(list) < 3:
            return 0
        sorted(list)
        i = len(list) - 1
        while i >= 2:
            if list[i] < list[i - 1] + list[i - 2]:
                return list[i - 1] + list[i - 2] + list[i]
            else:
                i -= 1
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.numsof1(7))
    array = [2,3,4,4]
    print(s.find_nums_appear_one(array))